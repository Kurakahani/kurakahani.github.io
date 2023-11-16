import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def format_duration(duration):
    hours = re.search(r"(\d+)H", duration)
    minutes = re.search(r"(\d+)M", duration)
    seconds = re.search(r"(\d+)S", duration)
    
    total_seconds = -1
    if hours:
        total_seconds += int(hours.group(1)) * 3600
    if minutes:
        total_seconds += int(minutes.group(1)) * 60
    if seconds:
        total_seconds += int(seconds.group(1))
    
    formatted_duration = str(timedelta(seconds=total_seconds))
    return formatted_duration

def generate_jekyll_posts(rss_file):
    tree = ET.parse(rss_file)
    root = tree.getroot()
    
    for item in root.findall(".//item"):
        metadata = {}
        metadata['title'] = item.find("title").text

        description_element = item.find("description")
        if description_element is not None and description_element.text is not None:
            metadata['description'] = description_element.text.replace("\n", "<br>")
        else:
            metadata['description'] = ""
        
        metadata['audio_url'] = item.find("enclosure").get("url")
        metadata['author'] = item.find("author").text
        metadata['published_date'] = item.find("pubDate").text.replace("T", " ").replace("Z", " +0000")
        namespace = {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}
        metadata['duration'] = format_duration(item.find("itunes:duration", namespaces=namespace).text)
        metadata['image'] = os.path.splitext(os.path.basename(item.find("itunes:image",namespaces=namespace).get("href")))[0]
        metadata['image-url'] = item.find("itunes:image", namespaces=namespace).get("href")

        if not os.path.exists("_posts"):
            os.makedirs("_posts")
        
        post_date = datetime.strptime(metadata['published_date'], "%Y-%m-%d %H:%M:%S %z")
        episode_number_match = re.search(r"Episode\s*(\d+)", metadata['title'])
        episode_number = episode_number_match.group(1) if episode_number_match else "Extra"

        if episode_number == "Extra":
            episode_numbers = re.sub(r'\W+', '-', metadata['title'].split("|")[0].strip().lower())
            episode_numbers = f"Extra-{episode_numbers}"
            post_file_name = post_date.strftime("%Y-%m-%d-") + f"Episode-{episode_numbers}.md"
        else:
            post_file_name = post_date.strftime("%Y-%m-%d-") + f"Episode-{episode_number}.md"
        post_file_path = os.path.join("_posts", post_file_name)
        
        with open(post_file_path, "w") as f:
            f.write("---\n")
            f.write(f"title: \"{metadata['title']}\"\n")
            f.write("layout: post\n")
            if episode_number == "Extra":
                f.write("categories: [Extra]\n")
            else:
                f.write("categories: [Main]\n")
            if episode_number == "Extra":
                f.write("type: extra\n")
            else:
                f.write("type: main\n")
            f.write(f"description: \"{metadata['description']}\"\n")
            f.write(f"file: {metadata['audio_url']}\n")
            f.write(f"length: \"{metadata['duration']}\"\n")
            f.write(f"videoid: {metadata['image']}\n")
            f.write(f"cover: {metadata['image-url']}\n")
            f.write("---\n")
