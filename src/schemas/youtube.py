from typing import List

from pydantic import BaseModel, Field


class VideoRequest(BaseModel):
    video_url: str = Field(
        ...,
        description="A valid YouTube video URL.",
        examples=[
            "https://youtu.be/dQw4w9WgXcQ"
        ],
    )


class VideoResponse(BaseModel):
    video_id: str = Field(
        ...,
        description="Extracted YouTube Video ID.",
        examples=[
            "dQw4w9WgXcQ"
        ],
    )

class TranscriptSnippet(BaseModel):
    text: str = Field(
        ...,
        description="Transcript text.",
    )

    start: float = Field(
        ...,
        description="Start time in seconds.",
    )

    duration: float = Field(
        ...,
        description="Duration in seconds.",
    )

class TranscriptResponse(BaseModel):
    video_id: str = Field(
        ...,
        description="YouTube Video ID.",
    )

    language: str = Field(
        ...,
        description="Transcript language.",
    )

    language_code: str = Field(
        ...,
        description="Language code.",
    )

    is_generated: bool = Field(
        ...,
        description="Whether the transcript was automatically generated.",
    )

    transcript: List[TranscriptSnippet] = Field(
        ...,
        description="List of transcript segments.",
    )