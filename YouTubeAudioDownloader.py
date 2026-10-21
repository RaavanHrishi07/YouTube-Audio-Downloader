
import argparse
import sys
from pathlib import Path

import yt_dlp


def download_audio(url, output_dir="."):
    """Download the best available audio stream for a video URL."""
    output_path = Path(output_dir).expanduser()

    try:
        output_path.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        print(f"Error creating output directory: {error}", file=sys.stderr)
        return 1

    options = {
        "format": "bestaudio/best",
        "outtmpl": str(output_path / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": False,
    }

    try:
        with yt_dlp.YoutubeDL(options) as downloader:
            info = downloader.extract_info(url, download=False)

            print("\n--- Video Details ---")
            print(f"Title: {info.get('title', 'Unknown')}")
            print(f"Uploader: {info.get('uploader', 'Unknown')}")
            print(f"Duration: {info.get('duration', 'Unknown')} seconds")
            print(f"Views: {info.get('view_count', 'Unknown')}")

            downloader.download([url])

        print(f"\nDownload completed. Output folder: {output_path.resolve()}")
        return 0

    except yt_dlp.utils.DownloadError as error:
        print(f"Download failed: {error}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as error:
        print(f"Unexpected error: {error}", file=sys.stderr)
        return 1


def main():
    parser = argparse.ArgumentParser(
        description="Download audio from a supported video URL."
    )
    parser.add_argument(
        "url",
        help="URL of the video you want to download",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="downloads",
        help="Directory where downloaded audio will be saved",
    )

    args = parser.parse_args()
    return download_audio(args.url, args.output_dir)


if __name__ == "__main__":
    raise SystemExit(main())
