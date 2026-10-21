
# YouTube Audio Downloader

A Python-based command-line application to download audio from supported video URLs using `yt-dlp`. It also includes a utility to convert audio files to MP3 format.

## Features

- Download the best available audio stream.
- Display video title, uploader, duration, and view count.
- Choose a custom output directory.
- Convert supported audio files to MP3.
- Handle missing files and download or conversion errors.
- Automated tests using pytest.

## Tech Stack

- Python 3.11+
- yt-dlp
- MoviePy 1.0.3
- FFmpeg
- pytest

## Project Structure

```text
YouTube-Audio-Downloader/
├── YouTubeAudioDownloader.py
├── WebmToMp3.py
├── requirements.txt
├── .gitignore
├── README.md
└── tests/
    └── test_converter.py
```

## Installation

### 1. Clone the repository

```powershell
git clone https://github.com/RaavanHrishi07/YouTube-Audio-Downloader.git
cd YouTube-Audio-Downloader
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Install FFmpeg

FFmpeg must be installed and accessible through your system PATH for audio conversion. Verify it with:

```powershell
ffmpeg -version
```

## Usage

### Download audio

Download audio from a supported video URL:

```powershell
python .\YouTubeAudioDownloader.py "VIDEO_URL"
```

By default, downloaded files are saved in the `downloads` directory.

To specify a different output directory:

```powershell
python .\YouTubeAudioDownloader.py "VIDEO_URL" --output-dir "my_audio"
```

### Convert an audio file to MP3

```powershell
python .\WebmToMp3.py "input.webm" "output.mp3"
```

The input must exist, and the output filename must end in `.mp3`.

## Run Tests

Run the automated test suite from the project root:

```powershell
python -m pytest -v
```

The converter tests cover missing input files, invalid output extensions, identical input/output paths, and successful conversion using a mocked audio clip.

## Responsible Use

Use this project only with content you own or are authorised to download. Follow the relevant platform's terms and applicable copyright laws.

## License

This project is currently available for personal and educational use. A formal open-source licence has not yet been added.


## Author

**Hrishikesh Sharma**

- GitHub: [@RaavanHrishi07](https://github.com/RaavanHrishi07)
- Repository: [YouTube Audio Downloader](https://github.com/RaavanHrishi07/YouTube-Audio-Downloader)
