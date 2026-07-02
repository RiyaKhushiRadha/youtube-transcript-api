from fastapi import FastAPI

app = FastAPI(
    title="YouTube Transcript Service",
    description="A FastAPI service to extract YouTube video transcripts.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to the YouTube Transcript Service!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }