from urllib.parse import urlparse, parse_qs


def extract_video_id(video_input: str) -> str:
    """
    Extract the YouTube video ID from a URL or a direct video ID.

    Args:
        video_input (str): A YouTube URL or video ID.

    Returns:
        str: The extracted video ID.
    """

    video_input = video_input.strip()

    return video_input