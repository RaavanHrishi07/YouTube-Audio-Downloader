
import argparse
import sys
from pathlib import Path

from moviepy.editor import AudioFileClip


def convert_to_mp3(input_file, output_file):
    source = Path(input_file).expanduser()
    destination = Path(output_file).expanduser()

    if not source.is_file():
        print(f"Error: Input file not found: {source}", file=sys.stderr)
        return 1

    if destination.suffix.lower() != ".mp3":
        print("Error: Output file must end with .mp3", file=sys.stderr)
        return 1

    if source.resolve() == destination.resolve():
        print("Error: Input and output paths must be different.", file=sys.stderr)
        return 1

    try:
        destination.parent.mkdir(parents=True, exist_ok=True)

        with AudioFileClip(str(source)) as clip:
            clip.write_audiofile(
                str(destination),
                codec="libmp3lame",
                logger=None,
            )

        print(f"Conversion successful: {destination.resolve()}")
        return 0

    except Exception as error:
        print(f"Conversion failed: {error}", file=sys.stderr)
        return 1


def main():
    parser = argparse.ArgumentParser(
        description="Convert an audio file to MP3."
    )
    parser.add_argument("input", help="Path to the source audio file")
    parser.add_argument("output", help="Path for the output MP3 file")
    args = parser.parse_args()

    return convert_to_mp3(args.input, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
