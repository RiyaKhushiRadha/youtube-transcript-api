from src.utils.youtube import extract_video_id
from src.exceptions.youtube import InvalidYouTubeURLException


test_inputs = [
    "dQw4w9WgXcQ",
    "https://youtu.be/dQw4w9WgXcQ",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "hello",
    "abcdefghijk",
    "abc@1234567",
    "",
]


for item in test_inputs:
    try:
        print(f"Input: {item}")
        print(f"Output: {extract_video_id(item)}")
    except InvalidYouTubeURLException as e:
        print(f"Error: {e}")

    print("-" * 40)