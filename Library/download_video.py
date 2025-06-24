#!/usr/bin/env python3
"""Download a YouTube video via URL using pytube."""

import argparse
import sys
from pathlib import Path

try:
    from pytube import YouTube
except ImportError:
    sys.exit("Please install pytube with: pip install pytube")


def download(url: str, output: Path) -> None:
    """Download the YouTube video at ``url`` to ``output`` directory."""
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
    stream.download(output_path=str(output))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a YouTube video")
    parser.add_argument("url", help="URL of the YouTube video")
    parser.add_argument(
        "--output",
        default=".",
        help="Output directory to save the video (default: current directory)",
    )
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)
    download(args.url, output_path)
    print(f"Downloaded video to: {output_path.resolve()}")
