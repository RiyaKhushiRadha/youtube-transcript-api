class InvalidYouTubeURLException(Exception):
    """Raised when the provided YouTube URL or video ID is invalid."""
    pass

class TranscriptNotAvailableException(Exception):
    """Raised when a transcript is not available for the requested video."""
    pass


class TranscriptDisabledException(Exception):
    """Raised when transcripts are disabled for the requested video."""
    pass

class TranscriptServiceException(Exception):
    """Raised for unexpected transcript service errors."""
    pass