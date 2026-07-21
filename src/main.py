from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.exceptions.youtube import (
    InvalidYouTubeURLException,
    TranscriptDisabledException,
    TranscriptNotAvailableException,
    TranscriptServiceException,
)

from src.api.routes import router

tags_metadata = [
    {
        "name": "General",
        "description": "General API information and health monitoring endpoints.",
    },
    {
        "name": "YouTube",
        "description": "Operations related to YouTube URL parsing and video information.",
    },
    {
        "name": "Transcript",
        "description": "Operations for fetching YouTube video transcripts.",
    },
]

app = FastAPI(
    title="YouTube Transcript API",
    description="""
A production-ready REST API built with FastAPI for extracting transcripts from YouTube videos.

## Features

- Extract transcripts from YouTube videos
- Supports manually created and auto-generated subtitles
- RESTful API
- Interactive Swagger Documentation
- Comprehensive error handling
- Automated testing with Pytest
- Cloud deployment on Render

This project was built as a backend engineering portfolio project following professional software development practices.
""",
    version="1.0.0",
    openapi_tags=tags_metadata,
    contact={
        "name": "Riya",
        "url": "https://github.com/RiyaKhushiRadha",
    },
    license_info={
        "name": "MIT License",
    },
    docs_url="/docs",
    redoc_url="/redoc",
)

@app.exception_handler(TranscriptNotAvailableException)
async def transcript_not_available_handler(
    request: Request,
    exc: TranscriptNotAvailableException,
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": str(exc),
        },
    )


@app.exception_handler(TranscriptDisabledException)
async def transcript_disabled_handler(
    request: Request,
    exc: TranscriptDisabledException,
):
    return JSONResponse(
        status_code=403,
        content={
            "detail": str(exc),
        },
    )

@app.exception_handler(TranscriptServiceException)
async def transcript_service_exception_handler(
    request: Request,
    exc: TranscriptServiceException,
):
    return JSONResponse(
        status_code=500,
        content={
            "detail": str(exc),
        },
    )

@app.exception_handler(InvalidYouTubeURLException)
async def invalid_youtube_url_handler(
    request: Request,
    exc: InvalidYouTubeURLException,
):
    return JSONResponse(
        status_code=400,
        content={
            "detail": str(exc),
        },
    )

app.include_router(router)