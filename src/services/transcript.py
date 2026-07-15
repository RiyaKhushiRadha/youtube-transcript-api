from youtube_transcript_api import YouTubeTranscriptApi


class TranscriptService:
    """
    Handles transcript-related business logic.
    """

    @staticmethod
    def get_transcript(video_id: str):
        """
        Fetch transcript for a given YouTube video ID.
        """

        transcript = YouTubeTranscriptApi().fetch(video_id)

        return {
            "video_id": transcript.video_id,
            "language": transcript.language,
            "language_code": transcript.language_code,
            "is_generated": transcript.is_generated,
            "transcript": [
                {
                    "text": snippet.text,
                    "start": snippet.start,
                    "duration": snippet.duration,
                }
                for snippet in transcript.snippets
            ],
        }