import argparse
import os
import email
from email import policy
from email.parser import BytesParser
from pathlib import Path

def parse_email(file_path):
    """Parses .eml file and extracts basic info."""
    if not os.path.isfile(file_path):
        print(f"[ERROR] File not found: {file_path}")
        return

    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    print("=" * 60)
    print(f"📧 From:    {msg['From']}")
    print(f"👤 To:      {msg['To']}")
    print(f"📅 Date:    {msg['Date']}")
    print(f"📝 Subject: {msg['Subject']}")
    print("-" * 60)

    # Try to extract plain text content
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                print("📄 Email Body (text/plain):\n")
                print(part.get_content())
                break
    else:
        print("📄 Email Body:\n")
        print(msg.get_content())

    print("=" * 60)

def main():
    parser = argparse.ArgumentParser(
        description="SentinelMail - Email Threat Inspection CLI Tool"
    )
    parser.add_argument(
        '--file', 
        required=True, 
        help='Path to the .eml email file to analyze'
    )
    args = parser.parse_args()
    parse_email(args.file)

if __name__ == "__main__":
    main()
