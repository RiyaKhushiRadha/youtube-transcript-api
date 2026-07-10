from exceptions.youtube import InvalidYouTubeURLException

try:
    raise InvalidYouTubeURLException("Invalid YouTube URL.")
except InvalidYouTubeURLException as e:
    print(e)