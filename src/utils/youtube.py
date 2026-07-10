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

    parsed_url = urlparse(video_input)

    if parsed_url.netloc == "youtu.be":
        return parsed_url.path.lstrip("/")

    if parsed_url.netloc in (
        "www.youtube.com",
        "youtube.com",
    ):
        query_params = parse_qs(parsed_url.query)

        if "v" in query_params:
            return query_params["v"][0]

    return video_input