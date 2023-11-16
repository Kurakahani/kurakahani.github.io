from PIL import Image, ImageFilter
import os
import yt_dlp
import googleapiclient.discovery
import googleapiclient.errors


# YouTube API key
API_KEY = os.environ.get("API_KEY")

# YouTube Data API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

def compress_audio(input_path, output_path, target_size):
    bitrate = 96  # Initial bitrate in kbps
    while True:
        os.system(f"ffmpeg -i {input_path} -c:a aac -b:a {bitrate}k -y {output_path}")
        compressed_size = os.path.getsize(output_path)
        if compressed_size <= target_size:
            break
        bitrate -= 16 # Reduce bitrate by 8 kbps for the next iteration


def convert_video_to_audio(video_id):
    # Download video as audio
    ydl_opts = {
        "format": "140",
        "outtmpl": f"audio_files/{video_id}.%(ext)s",
        "writethumbnail": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"https://www.youtube.com/watch?v={video_id}"])
        
    # Compress the audio file
    audio_path = f"audio_files/{video_id}.m4a"
    
    # Compress audio if larger than 50 MiB
    audio_size = os.path.getsize(audio_path)
    if audio_size > 50 * 1024 * 1024:  # If larger than 50 MiB
        compressed_audio_path = f"audio_files/{video_id}_compressed.m4a"
        compress_audio(audio_path, compressed_audio_path, 50 * 1024 * 1024)
        
        # Delete the original audio file
        os.remove(audio_path)
        
        # Rename the compressed audio file to the original name
        os.rename(compressed_audio_path, audio_path)
    
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

            # Call make_square_cover() here
        make_square_cover(thumbnail_destination_path, thumbnail_destination_path)

def extract_metadata(video_id):
    try:
        # Fetch video metadata using the YouTube Data API
        video_response = youtube.videos().list(
            part="snippet,contentDetails",  # Fetch contentDetails as well
            id=video_id
        ).execute()

        video_data = video_response.get("items", [])[0]

        snippet = video_data["snippet"]
        content_details = video_data["contentDetails"]

        # Extract metadata
        metadata = {
            "title": snippet["title"],
            "description": snippet["description"],
            "author": "Prabin Buddhacharya",
            "email": "kurakahani@gmail.com",
            "image": f"images/{video_id}",
            "language": "Nepali",
            "audio_url": f"audio_files/{video_id}.m4a",
            "published_date": snippet["publishedAt"],
            "duration": content_details["duration"],  # Fetch duration from contentDetails
        }
        return metadata

    except googleapiclient.errors.HttpError as e:
        print("An error occurred:", e)
        return {}

def make_square_cover(input_image_path, output_image_path, blur_radius=20):
    # Open the input image
    img = Image.open(input_image_path)
    
    # Calculate the dimensions for the square cover
    width, height = img.size
    new_size = max(width, height)
    
    # Create a blank white canvas of the new size
    canvas = Image.new('RGBA', (new_size, new_size), (0, 0, 0, 0))
    
    # Calculate the position to paste the original image
    x_offset = (new_size - width) // 2
    y_offset = (new_size - height) // 2
    
    # Paste the original image onto the canvas
    canvas.paste(img, (x_offset, y_offset))
    
    # Apply a blur filter to the top and bottom parts of the canvas
    blurred_canvas = canvas.copy()
    top_box = (0, 0, new_size, height // 4)
    bottom_box = (0, 3 * height // 4, new_size, new_size)
    blurred_canvas.crop(top_box).filter(ImageFilter.GaussianBlur(blur_radius)).paste(canvas.crop(top_box), (0, 0))
    blurred_canvas.crop(bottom_box).filter(ImageFilter.GaussianBlur(blur_radius)).paste(canvas.crop(bottom_box), (0, 3 * height // 4))
    
    # Save the final square cover image
    blurred_canvas.save(output_image_path)