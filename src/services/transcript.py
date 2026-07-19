from youtube_transcript_api import YouTubeTranscriptApi

from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
)

from src.exceptions.youtube import (
    TranscriptDisabledException,
    TranscriptNotAvailableException,
    TranscriptServiceException,
)

class TranscriptService:
    """
    Handles transcript-related business logic.
    """

    @staticmethod
    def get_transcript(video_id: str):
        """
        Fetch transcript for a given YouTube video ID.
        """

        try:
            fetched = YouTubeTranscriptApi().fetch(video_id)

            return {
                "video_id": fetched.video_id,
                "language": fetched.language,
                "language_code": fetched.language_code,
                "is_generated": fetched.is_generated,
                "transcript": [
                    {
                        "text": snippet.text,
                        "start": snippet.start,
                        "duration": snippet.duration,
                    }
                    for snippet in fetched.snippets
                ],
            }

        except NoTranscriptFound:
            raise TranscriptNotAvailableException(
                "No transcript is available for this video."
            )

        except TranscriptsDisabled:
            raise TranscriptDisabledException(
                "Transcripts are disabled for this video."
            )
        
        except Exception as exc:
            raise TranscriptServiceException(
                "An unexpected error occurred while fetching the transcript."
            ) from exc