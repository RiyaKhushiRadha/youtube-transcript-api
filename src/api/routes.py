from fastapi import APIRouter

from src.schemas.youtube import VideoRequest, VideoResponse
from src.utils.youtube import extract_video_id
from src.services.transcript import TranscriptService

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Welcome to the YouTube Transcript Service!"
    }


@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@router.post(
    "/parse",
    response_model=VideoResponse,
)
def parse_video(request: VideoRequest):
    video_id = extract_video_id(request.video_url)

    return VideoResponse(video_id=video_id)

@router.post("/transcript")
def get_transcript(request: VideoRequest):
    video_id = extract_video_id(request.video_url)

    transcript = TranscriptService.get_transcript(video_id)

    return transcript