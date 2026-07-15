from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="YouTube Transcript Service",
    description="A FastAPI service to extract YouTube video transcripts.",
    version="0.1.0",
)

app.include_router(router)