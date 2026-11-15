#!/usr/bin/env bash
# Run only in the clean, disposable Actions checkout of current main.
set -euo pipefail
if [ "$#" -ne 1 ]; then
  echo 'Usage: merge_pending_incidents.sh <pending-ref>' >&2
  exit 2
fi
if [ -n "$(git status --porcelain)" ]; then
  echo 'Refusing to merge pending incidents into a dirty checkout.' >&2
  exit 1
fi
# Full history is required to find the true common ancestor. Never resolve conflicts
# automatically: set -e stops the workflow before any remote branch is updated.
git -c user.name='Incident refresh' -c user.email='incident-refresh@example.invalid' \
  merge --no-commit --no-ff "$1"
# Keep the merged working files as a proposed diff against main, without moving
# HEAD or leaving MERGE_HEAD/index state for create-pull-request to interpret.
git reset --mixed HEAD
