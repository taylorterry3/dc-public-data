"""Replay public ArcGIS responses without network calls or real sleeps."""

import io
import json

from scripts import refresh_incidents as refresh


def test_json_service_timeout_is_retried(monkeypatch):
    responses = [
        {"error": {"code": 503, "message": "Error handling service request :"
                   "Wait timeout for the request exceeded.", "details": []}},
        {"objectIds": [1, 2]},
    ]
    attempts, delays = [], []

    def urlopen(url, timeout):
        attempts.append(url)
        return io.BytesIO(json.dumps(responses.pop(0)).encode())

    monkeypatch.setattr(refresh, "urlopen", urlopen)
    monkeypatch.setattr(refresh.time, "sleep", delays.append)
    assert refresh.request_json("https://example.test/query", returnIdsOnly="true") == {
        "objectIds": [1, 2],
    }
    assert len(attempts) == 2
    assert delays == [1]


def install_responses(monkeypatch, responses):
    attempts, delays = [], []

    def urlopen(url, timeout):
        attempts.append(url)
        value = responses.pop(0)
        if isinstance(value, Exception):
            raise value
        return io.BytesIO(value if isinstance(value, bytes) else json.dumps(value).encode())

    monkeypatch.setattr(refresh, "urlopen", urlopen)
    monkeypatch.setattr(refresh.time, "sleep", delays.append)
    return attempts, delays


def test_persistent_json_timeout_exhausts_budget(monkeypatch):
    import pytest

    error = {"error": {"code": 503, "message": "Wait timeout for the request exceeded."}}
    attempts, delays = install_responses(monkeypatch, [error] * 3)
    with pytest.raises(ValueError, match="Wait timeout"):
        refresh.request_json("https://example.test/query")
    assert len(attempts) == 3 and delays == [1, 2]


def test_permanent_arcgis_error_fails_immediately(monkeypatch):
    import pytest

    attempts, delays = install_responses(monkeypatch, [
        {"error": {"code": 400, "message": "Invalid query"}},
    ])
    with pytest.raises(ValueError, match="Invalid query"):
        refresh.request_json("https://example.test/query")
    assert len(attempts) == 1 and delays == []


def test_http_503_then_success(monkeypatch):
    from urllib.error import HTTPError

    attempts, delays = install_responses(monkeypatch, [
        HTTPError("https://example.test/query", 503, "Service unavailable", {}, None),
        {"objectIds": [1]},
    ])
    assert refresh.request_json("https://example.test/query") == {"objectIds": [1]}
    assert len(attempts) == 2 and delays == [1]


def test_http_404_does_not_retry(monkeypatch):
    from urllib.error import HTTPError

    import pytest

    attempts, delays = install_responses(monkeypatch, [
        HTTPError("https://example.test/query", 404, "Not found", {}, None),
    ])
    with pytest.raises(HTTPError):
        refresh.request_json("https://example.test/query")
    assert len(attempts) == 1 and delays == []


def test_network_timeout_and_invalid_json_then_success(monkeypatch):
    attempts, delays = install_responses(monkeypatch, [
        TimeoutError("read timed out"), b"temporarily unavailable", {"objectIds": [1]},
    ])
    assert refresh.request_json("https://example.test/query") == {"objectIds": [1]}
    assert len(attempts) == 3 and delays == [1, 2]


def test_persistent_http_503_exhausts_budget(monkeypatch):
    from urllib.error import HTTPError

    import pytest

    attempts, delays = install_responses(monkeypatch, [
        HTTPError("https://example.test/query", 503, "Service unavailable", {}, None)
        for _ in range(3)
    ])
    with pytest.raises(HTTPError):
        refresh.request_json("https://example.test/query")
    assert len(attempts) == 3 and delays == [1, 2]
