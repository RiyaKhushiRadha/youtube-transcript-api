from fastapi import APIRouter

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