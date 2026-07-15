from pprint import pprint

from src.services.transcript import TranscriptService


VIDEO_ID = "dQw4w9WgXcQ"

transcript = TranscriptService.get_transcript(VIDEO_ID)

print(type(transcript))
print()

pprint(transcript)