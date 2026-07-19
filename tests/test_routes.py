from unittest.mock import patch

from fastapi.testclient import TestClient

from src.main import app
from src.exceptions.youtube import TranscriptNotAvailableException

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "healthy"
    }

def test_invalid_youtube_url():
    response = client.post(
        "/transcript",
        json={
            "video_url": "https://google.com"
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "Invalid YouTube URL or Video ID."
    }

@patch("src.api.routes.TranscriptService.get_transcript")
def test_transcript_not_available(mock_get_transcript):
    mock_get_transcript.side_effect = TranscriptNotAvailableException(
        "No transcript is available for this video."
    )

    response = client.post(
        "/transcript",
        json={
            "video_url": "https://youtu.be/dQw4w9WgXcQ"
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "No transcript is available for this video."
    }