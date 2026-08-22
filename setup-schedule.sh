#!/usr/bin/env bash
# setup-schedule.sh — Install a cron job to run the brief every weekday at 3pm
#
# Adjust BRIEF_DIR and RUN_TIME to match your setup.
# Run once: bash setup-schedule.sh

BRIEF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RUN_TIME="0 15 * * 1-5"  # 3pm Mon-Fri
LOG_DIR="$BRIEF_DIR/logs"
LOG_FILE="$LOG_DIR/brief.log"

mkdir -p "$LOG_DIR"

CRON_CMD="$RUN_TIME cd \"$BRIEF_DIR\" && bash run.sh --headless >> \"$LOG_FILE\" 2>&1"

# Check if job already exists
if crontab -l 2>/dev/null | grep -qF "$BRIEF_DIR"; then
  echo "Cron job already exists for this project."
  crontab -l | grep "$BRIEF_DIR"
else
  (crontab -l 2>/dev/null; echo "$CRON_CMD") | crontab -
  echo "Cron job installed: $RUN_TIME"
  echo "Logs: $LOG_FILE"
fi
