import yt_dlp
import googleapiclient.discovery
import googleapiclient.errors

# YouTube API key
API_KEY = "YOUR_YOUTUBE_API_KEY"

# YouTube Data API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

def convert_video_to_audio(video_id):
    # Download video as audio
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"audio_files/{video_id}.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"https://www.youtube.com/watch?v={video_id}"])

    # Download video thumbnail as PNG
    ydl_opts_thumbnail = {
        "format": "best",  # Specify the desired format for the thumbnail
        "outtmpl": f"images/{video_id}.png"
    }
    with yt_dlp.YoutubeDL(ydl_opts_thumbnail) as ydl_thumbnail:
        ydl_thumbnail.download([f"https://www.youtube.com/watch?v={video_id}"])

def extract_metadata(video_id):
    try:
        # Fetch video metadata using the YouTube Data API
        video_response = youtube.videos().list(
            part="snippet",
            id=video_id
        ).execute()

        video_data = video_response.get("items", [])[0]["snippet"]

        # Extract metadata
        metadata = {
            "title": video_data["title"],
            "description": video_data["description"],
            "author": "Prabin Buddhacharya",
            "email": "kurakahani@gmail.com",
            "image": f"images/{video_id}",
            "language": "Nepali",
            "audio_url": f"audio_files/{video_id}.mp3",
            "published_date": video_data["publishedAt"],
            "duration": video_data["duration"]
        }
        return metadata

    except googleapiclient.errors.HttpError as e:
        print("An error occurred:", e)
        return {}