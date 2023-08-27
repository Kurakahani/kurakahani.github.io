from PIL import Image
import os
import yt_dlp
import googleapiclient.discovery
import googleapiclient.errors


# YouTube API key
API_KEY = os.environ.get("API_KEY")

# YouTube Data API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

def compress_audio(input_path, output_path, target_size):
    bitrate = 128  # Initial bitrate in kbps
    while True:
        os.system(f"ffmpeg -i {input_path} -c:a aac -b:a {bitrate}k {output_path}")
        compressed_size = os.path.getsize(output_path)
        if compressed_size <= target_size:
            break
        bitrate -= 8  # Reduce bitrate by 8 kbps for the next iteration


def convert_video_to_audio(video_id):
    # Download video as audio
    ydl_opts = {
        "format": "140",
        "outtmpl": f"audio_files/{video_id}.%(ext)s",
        "writethumbnail": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"https://www.youtube.com/watch?v={video_id}"])
        
    # Determine the thumbnail format
    thumbnail_format = None
    for filename in os.listdir('audio_files'):
        if filename.startswith(video_id) and filename != f"{video_id}.m4a":
            thumbnail_format = filename.split('.')[-1]
            break
            
    if thumbnail_format is not None:
        thumbnail_source_path = f"audio_files/{video_id}.{thumbnail_format}"
        thumbnail_destination_path = f"images/{video_id}.jpg"
        
        # Convert the thumbnail to JPG format if it's not already
        if thumbnail_format != 'jpg':
            img = Image.open(thumbnail_source_path)
            img.save(thumbnail_destination_path, format="JPEG")  # Save as JPG format
            os.remove(thumbnail_source_path)  # Remove the original file
        else:
            os.rename(thumbnail_source_path, thumbnail_destination_path)  # Just move if already JPG

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
            "audio_url": f"audio_files/{video_id}.m4a",
            "published_date": video_data["publishedAt"]
        }
        return metadata

    except googleapiclient.errors.HttpError as e:
        print("An error occurred:", e)
        return {}