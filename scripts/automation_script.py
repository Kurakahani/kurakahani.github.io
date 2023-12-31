import os
from datetime import datetime
from xml.etree import ElementTree as ET
import googleapiclient.discovery
import googleapiclient.errors
from conversion_script import convert_video_to_audio, extract_metadata
from rss_feed_generator import generate_rss_entry, update_rss_feed, rss_copy
from generate_post import generate_jekyll_posts

# YouTube API key
API_KEY = os.environ.get("API_KEY")

# YouTube Data API client
youtube = googleapiclient.discovery.build(
    "youtube", "v3", developerKey=API_KEY)

# Kurakahani Podcast YouTube channel ID
CHANNEL_ID = "UC522A4Nx21ApYqwZzAiwhRg"

# Kurakani rss filename
rss_file = "rss_feed.xml"

def get_new_videos():
    try:
        next_page_token = None
        while True:
            # Perform a search for new podcast videos on Kurakahani Podcast channel
            search_response = youtube.search().list(
                q="",
                channelId=CHANNEL_ID,
                order="date",
                type="video",
                part="id",
                maxResults=50,  # Adjust as needed, 50 is the maximum allowed
                pageToken=next_page_token
            ).execute()
            # Check if there are more pages
            next_page_token = search_response.get("nextPageToken")

            if not next_page_token:
                break  # No more pages, exit the loop

        # Extract video IDs from search results
        video_ids = [item["id"]["videoId"]
                     for item in search_response.get("items", [])]

        # Exclude the specific video ID
        video_ids = [vid for vid in video_ids]

        return video_ids

    except googleapiclient.errors.HttpError as e:
        print("An error occurred:", e)
        return []

# def premiere_check():
    #To be implemented


def main():
    # Load existing video IDs from the available_podcasts.txt file
    existing_video_ids = []
    if os.path.exists("available_podcasts.txt"):
        with open("available_podcasts.txt", "r", encoding="utf-8") as f:
            existing_video_ids = [line.strip() for line in f.readlines()]

    # Get new video IDs
    new_video_ids = get_new_videos()

    # Filter out already existing videos
    new_video_ids = [
        vid for vid in new_video_ids if vid not in existing_video_ids]

    if new_video_ids:
        # Update the available_podcasts.txt file with new video IDs
        with open("available_podcasts.txt", "a") as f:
            for vid in new_video_ids:
                f.write(vid + "\n")

        new_video_ids.reverse()

        # Process new videos
        for video_id in new_video_ids:
            # Call conversion_script to convert video to audio
            convert_video_to_audio(video_id)

            # Call extract_metadata to get video metadata
            metadata = extract_metadata(video_id)

            # Call rss_feed_generator to update the RSS feed
            generate_rss_entry(metadata)
            update_rss_feed(metadata)

    generate_jekyll_posts(rss_file)
    rss_copy()

if __name__ == "__main__":
    main()
