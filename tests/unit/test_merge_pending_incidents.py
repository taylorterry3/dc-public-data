"""Exercise the workflow's merge step against real Git histories."""

import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[2] / "scripts/merge_pending_incidents.sh"


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def history(root, *, conflict=False):
    git(root, "init", "-b", "main")
    git(root, "config", "user.name", "Test")
    git(root, "config", "user.email", "test@example.com")
    (root / "historical.csv").write_text("accepted original\n")
    (root / "recent.csv").write_text("recent original\n")
    git(root, "add", ".")
    git(root, "commit", "-m", "base")
    git(root, "switch", "-c", "pending")
    target = "historical.csv" if conflict else "recent.csv"
    (root / target).write_text("pending update\n")
    git(root, "add", ".")
    git(root, "commit", "-m", "pending")
    pending_head = git(root, "rev-parse", "HEAD")
    git(root, "switch", "main")
    (root / "historical.csv").write_text("accepted correction with added rows\n")
    git(root, "add", ".")
    git(root, "commit", "-m", "accepted correction")
    return git(root, "rev-parse", "HEAD"), pending_head


def test_preserves_new_accepted_history_and_pending_update(tmp_path):
    head, pending = history(tmp_path)
    subprocess.run(["bash", str(SCRIPT), "pending"], cwd=tmp_path, check=True)
    assert (tmp_path / "historical.csv").read_text() == "accepted correction with added rows\n"
    assert (tmp_path / "recent.csv").read_text() == "pending update\n"
    assert git(tmp_path, "rev-parse", "HEAD") == head
    assert git(tmp_path, "rev-parse", "pending") == pending
    assert git(tmp_path, "diff", "--name-only") == "recent.csv"
    assert git(tmp_path, "diff", "--cached", "--name-only") == ""
    assert not (tmp_path / ".git/MERGE_HEAD").exists()


def test_conflicting_accepted_correction_stops_without_changing_refs(tmp_path):
    head, pending = history(tmp_path, conflict=True)
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.run(["bash", str(SCRIPT), "pending"], cwd=tmp_path, check=True)
    assert git(tmp_path, "rev-parse", "HEAD") == head
    assert git(tmp_path, "rev-parse", "pending") == pending
    assert git(tmp_path, "diff", "--name-only", "--diff-filter=U") == "historical.csv"
