import pytest

from src.utils.youtube import extract_video_id
from src.exceptions.youtube import InvalidYouTubeURLException


def test_extract_video_id_from_standard_url():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    assert extract_video_id(url) == "dQw4w9WgXcQ"


def test_extract_video_id_from_short_url():
    url = "https://youtu.be/dQw4w9WgXcQ"

    assert extract_video_id(url) == "dQw4w9WgXcQ"


def test_invalid_youtube_url():
    url = "https://google.com"

    with pytest.raises(InvalidYouTubeURLException):
        extract_video_id(url)