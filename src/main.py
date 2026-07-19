from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.exceptions.youtube import (
    InvalidYouTubeURLException,
    TranscriptDisabledException,
    TranscriptNotAvailableException,
    TranscriptServiceException,
)

from src.api.routes import router

app = FastAPI(
    title="YouTube Transcript Service",
    description="A FastAPI service to extract YouTube video transcripts.",
    version="0.1.0",
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