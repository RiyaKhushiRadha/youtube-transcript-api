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