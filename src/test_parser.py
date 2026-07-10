from utils.youtube import extract_video_id

print(extract_video_id("abc123"))
print(extract_video_id("   abc123   "))
print(extract_video_id("https://youtu.be/dQw4w9WgXcQ"))
print(extract_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
print(extract_video_id("https://youtube.com/watch?v=dQw4w9WgXcQ"))
print(extract_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=45s"))