from fastapi import APIRouter

from src.schemas.youtube import (
    TranscriptResponse,
    VideoRequest,
    VideoResponse,
)
from src.utils.youtube import extract_video_id
from src.services.transcript import TranscriptService

router = APIRouter()


@router.get(
    "/",
    tags=["General"],
    summary="API Information",
    description="Returns basic information about the API including version, status, and available endpoints.",
)
def root():
    return {
        "service": "YouTube Transcript API",
        "version": "1.0.0",
        "status": "online",
        "documentation": "/docs",
        "health_check": "/health",
    }


@router.get(
    "/health",
    tags=["General"],
    summary="Health Check",
    description="Checks whether the API is running correctly.",
)
def health_check():
    return {
        "status": "healthy"
    }

@router.post(
    "/parse",
    response_model=VideoResponse,
    tags=["YouTube"],
    summary="Extract Video ID",
    description="Extracts the YouTube Video ID from a valid YouTube URL.",
    responses={
        400: {
            "description": "Invalid YouTube URL or Video ID.",
        },
    },
)
def parse_video(request: VideoRequest):
    video_id = extract_video_id(request.video_url)

    return VideoResponse(video_id=video_id)

@router.post(
    "/transcript",
    response_model=TranscriptResponse,
    tags=["Transcript"],
    summary="Fetch Transcript",
    description="Fetches the transcript of a YouTube video using its URL.",
    responses={
        400: {
            "description": "Invalid YouTube URL or Video ID.",
        },
        403: {
            "description": "Transcripts are disabled for this video.",
        },
        404: {
            "description": "No transcript is available for this video.",
        },
    },
)
def get_transcript(request: VideoRequest):
    video_id = extract_video_id(request.video_url)

    transcript = TranscriptService.get_transcript(video_id)

    return transcript