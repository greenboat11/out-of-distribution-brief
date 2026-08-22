"""
send_brief.py — Send the most recent Out of Distribution brief via Outlook on Windows.

Usage:
    python scripts/send_brief.py
    python scripts/send_brief.py --dry-run     # write preview to out/*.preview.html
    python scripts/send_brief.py --file out/2026-08-22-brief.html

Recipient is read from BRIEF_RECIPIENT env var, or a .env file in the project root.
"""

import argparse
import os
import sys
from pathlib import Path

OUT_DIR = Path(__file__).parent.parent / "out"


def load_recipient() -> str:
    recipient = os.environ.get("BRIEF_RECIPIENT", "").strip()
    if not recipient:
        # Try .env file in project root
        env_file = Path(__file__).parent.parent / ".env"
        if env_file.exists():
            for line in env_file.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("BRIEF_RECIPIENT="):
                    recipient = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
    if not recipient:
        raise ValueError(
            "No recipient configured. Set BRIEF_RECIPIENT env var or add "
            "BRIEF_RECIPIENT=you@example.com to a .env file in the project root."
        )
    return recipient


def find_latest_html() -> Path:
    files = sorted(OUT_DIR.glob("*-brief.html"))
    if not files:
        raise FileNotFoundError(f"No brief HTML files found in {OUT_DIR}")
    return files[-1]


def find_latest_md() -> Path:
    files = sorted(OUT_DIR.glob("*-brief.md"))
    if not files:
        raise FileNotFoundError(f"No brief markdown files found in {OUT_DIR}")
    return files[-1]


def extract_date_from_filename(path: Path) -> str:
    stem = path.stem  # e.g. "2026-08-22-brief"
    parts = stem.split("-")
    if len(parts) >= 3:
        return f"{parts[0]}-{parts[1]}-{parts[2]}"
    return stem


def send_via_outlook(subject: str, html_body: str, recipient: str) -> None:
    try:
        import win32com.client  # type: ignore
    except ImportError:
        raise ImportError(
            "pywin32 is required for Outlook sending: pip install pywin32"
        )

    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.HTMLBody = html_body
    mail.Send()


def main() -> None:
    parser = argparse.ArgumentParser(description="Send Out of Distribution brief via Outlook.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print subject and file path without sending")
    parser.add_argument("--file", help="Specific HTML brief file (default: most recent)")
    args = parser.parse_args()

    html_path = Path(args.file) if args.file else find_latest_html()
    if not html_path.exists():
        print(f"Error: File not found: {html_path}", file=sys.stderr)
        sys.exit(1)

    date_str = extract_date_from_filename(html_path)
    subject = f"Out of Distribution — {date_str}"
    html_body = html_path.read_text(encoding="utf-8")

    if args.dry_run:
        print(f"Subject : {subject}")
        print(f"File    : {html_path}")
        print(f"Size    : {len(html_body):,} bytes")
        print("(dry run — not sent)")
        return

    recipient = load_recipient()
    send_via_outlook(subject, html_body, recipient)
    print(f"Sent    : {subject}")
    print(f"To      : {recipient}")
    print(f"From    : {html_path}")


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError, ImportError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
