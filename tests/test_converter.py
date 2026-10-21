
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch

from WebmToMp3 import convert_to_mp3


def test_missing_input_file_returns_error(tmp_path):
    input_file = tmp_path / "missing.webm"
    output_file = tmp_path / "output.mp3"

    result = convert_to_mp3(input_file, output_file)

    assert result == 1
    assert not output_file.exists()


def test_invalid_output_extension_returns_error(tmp_path):
    input_file = tmp_path / "audio.webm"
    input_file.touch()
    output_file = tmp_path / "output.wav"

    result = convert_to_mp3(input_file, output_file)

    assert result == 1


def test_input_and_output_same_path_returns_error(tmp_path):
    audio_file = tmp_path / "audio.mp3"
    audio_file.touch()

    result = convert_to_mp3(audio_file, audio_file)

    assert result == 1


def test_successful_conversion(tmp_path):
    input_file = tmp_path / "audio.webm"
    output_file = tmp_path / "output.mp3"
    input_file.touch()

    mock_clip = MagicMock()

    with patch("WebmToMp3.AudioFileClip") as mock_audio:
        mock_audio.return_value.__enter__.return_value = mock_clip

        result = convert_to_mp3(input_file, output_file)

    assert result == 0
    mock_audio.assert_called_once_with(str(input_file))
    mock_clip.write_audiofile.assert_called_once_with(
        str(output_file),
        codec="libmp3lame",
        logger=None,
    )
