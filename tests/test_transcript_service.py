from unittest.mock import MagicMock, patch

from src.services.transcript import TranscriptService


@patch("src.services.transcript.YouTubeTranscriptApi")
def test_get_transcript(mock_api):
    fake_snippet = MagicMock()
    fake_snippet.text = "Hello World"
    fake_snippet.start = 0.0
    fake_snippet.duration = 5.0

    fake_transcript = MagicMock()
    fake_transcript.video_id = "abc123"
    fake_transcript.language = "English"
    fake_transcript.language_code = "en"
    fake_transcript.is_generated = False
    fake_transcript.snippets = [fake_snippet]

    mock_api.return_value.fetch.return_value = fake_transcript

    result = TranscriptService.get_transcript("abc123")

    assert result["video_id"] == "abc123"
    assert result["language"] == "English"
    assert result["transcript"][0]["text"] == "Hello World"