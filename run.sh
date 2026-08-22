#!/usr/bin/env bash
# run.sh — Launch the Out of Distribution brief orchestrator
#
# Usage:
#   ./run.sh              # Interactive Claude Code session
#   ./run.sh --headless   # Non-interactive (for cron/scheduled runs)
#
# Prerequisites:
#   - Claude Code CLI installed: npm install -g @anthropic-ai/claude-code
#   - Authenticated: claude login
#   - BRIEF_RECIPIENT env var set (or .env file in project root)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Load .env if present
if [[ -f ".env" ]]; then
  export $(grep -v '^#' .env | xargs)
fi

if [[ "${1:-}" == "--headless" ]]; then
  echo "[$(date -Iseconds)] Starting headless brief run..."
  claude --dangerously-skip-permissions -p \
    "Run the daily Out of Distribution brief as described in CLAUDE.md. Follow the run procedure exactly: read state/last_run.json, spawn all 7 topical agents in parallel via the Task tool, then the synthesizer, then the editor. Write output to ./out/ and update state files. Then run: python scripts/send_brief.py"
else
  echo "Launching Claude Code for Out of Distribution brief..."
  echo "The orchestrator instructions are in CLAUDE.md."
  claude
fi
