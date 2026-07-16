from typing import List

from pydantic import BaseModel


class VideoRequest(BaseModel):
    """
    Request model for a YouTube video.
    """

    video_url: str


class VideoResponse(BaseModel):
    """
    Response model containing the extracted video ID.
    """

    video_id: str

class TranscriptSnippet(BaseModel):
    text: str
    start: float
    duration: float

class TranscriptResponse(BaseModel):
    video_id: str
    language: str
    language_code: str
    is_generated: bool
    transcript: List[TranscriptSnippet]