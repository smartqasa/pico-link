#!/bin/bash
set -e

REPO_EXPECTED="smartqasa/pico-link"

echo "Promoting beta → main for $REPO_EXPECTED..."

# ------------------------------------------------
# Repo sanity checks
# ------------------------------------------------

# Must be inside a git repo
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "ERROR: Not inside a Git repository."
    exit 1
fi

# Ensure correct repository
REMOTE_URL=$(git remote get-url origin 2>/dev/null || true)

if [[ -z "$REMOTE_URL" ]]; then
    echo "ERROR: No 'origin' remote configured."
    exit 1
fi

if [[ "$REMOTE_URL" != *"$REPO_EXPECTED"* ]]; then
    echo "ERROR: This does not appear to be the $REPO_EXPECTED repository."
    echo "Found origin: $REMOTE_URL"
    exit 1
fi

# Ensure clean working tree
if [[ -n "$(git status --porcelain)" ]]; then
    echo "ERROR: Working tree not clean. Commit or stash changes first."
    exit 1
fi

# Fetch latest refs
echo "Fetching latest from origin..."
git fetch origin

# Ensure remote branches exist
if ! git show-ref --verify --quiet refs/remotes/origin/beta; then
    echo "ERROR: origin/beta does not exist."
    exit 1
fi

if ! git show-ref --verify --quiet refs/remotes/origin/main; then
    echo "ERROR: origin/main does not exist."
    exit 1
fi

# Ensure local beta exists
if ! git show-ref --verify --quiet refs/heads/beta; then
    echo "Local beta branch missing — creating from origin/beta"
    git branch beta origin/beta
fi

# Ensure local main exists
if ! git show-ref --verify --quiet refs/heads/main; then
    echo "Local main branch missing — creating from origin/main"
    git branch main origin/main
fi

# ------------------------------------------------
# Promotion
# ------------------------------------------------

echo "Updating local beta..."
git switch beta
git pull --ff-only origin beta

echo "Switching to main..."
git switch main

echo "Resetting main to origin/beta..."
git reset --hard origin/beta

echo "Pushing updated main to origin..."
git push --force-with-lease origin main

echo "Switching back to beta..."
git switch beta

echo "✓ Promotion complete. You are now back on beta."
