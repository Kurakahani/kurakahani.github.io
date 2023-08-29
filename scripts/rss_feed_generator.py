import re
import os

def generate_rss_entry(metadata):
    rss_entry = f"""
        <item>
            <title>{metadata['title']}</title>
            <description>{metadata['description']}</description>
            <enclosure url="https://github.com/Kurakahani/Kurakahani.github.io/raw/main/{metadata['audio_url']}" length="1" type="audio/mpeg"/>
            <author>{metadata['author']}</author>
            <pubDate>{metadata['published_date']}</pubDate>
            <guid>https://github.com/Kurakahani/Kurakahani.github.io/raw/main/{metadata['audio_url']}</guid>
            <itunes:author>{metadata['author']}</itunes:author>
            <itunes:explicit>no</itunes:explicit>
            <itunes:image href="https://raw.githubusercontent.com/Kurakahani/Kurakahani.github.io/main/{metadata['image']}.jpg"/>
            <itunes:duration>{metadata['duration']}</itunes:duration>
        </item>
    """
    return rss_entry


def update_rss_feed(metadata):
    rss_header = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
<channel>
    <title>Kurakahani Podcast</title>
    <link>https://www.youtube.com/@KuraKahaniPodcast</link>
    <language>ne</language>
    <itunes:author>Prabin Buddhacharya</itunes:author>
    <itunes:category text="Entertainment"/>
    <itunes:image href="https://raw.githubusercontent.com/Kurakahani/Kurakahani.github.io/main/images/logo.jpg"/>
    <description>We are Kurakahani Podcast channel. We do podcast with different people of different background. Trying to hear and share the story of them.
    We are team of three individuals with different interest but the talking and sharing of different idea bought us together and here we are to share and hear the story of us and our friends guest that shows up on the podcast.
    Kurakahani is a platform to share the feelings, ideas, gossip and many more.
    Support us by anyway possible to grow.
    Thank you</description>
    <itunes:explicit>no</itunes:explicit>
        """
    rss_footer = """
</channel>
</rss>"""
    # Create a list to store the generated <item> elements
    rss_entries = []

    # Add the new <item> element to the list
    rss_entries.append(generate_rss_entry(metadata))

    # Read the existing <item> elements from the rss_feed.xml file (if it exists)
    try:
        with open("rss_feed.xml", "r", encoding="utf-8") as f:
            rss_content = f.read()

        # Extract the existing <item> elements
        existing_items = re.findall(
            r"<item>.*?</item>", rss_content, re.DOTALL)

        # Add the existing <item> elements to the list
        rss_entries.extend(existing_items)
    except FileNotFoundError:
        pass  # No need to do anything if the file doesn't exist yet

    # Sort the <item> elements based on pubDate
    rss_entries.sort(key=lambda item: re.search(
        r"<pubDate>(.*?)</pubDate>", item).group(1), reverse=True)

    # Combine all <item> elements to recreate the rss_feed.xml content
    rss_content = rss_header + "\n".join(rss_entries) + rss_footer

    # Write the sorted content to the rss_feed.xml file
    with open("rss_feed.xml", "w", encoding="utf-8") as f:
        f.write(rss_content)


def rss_copy():
    source_file = "rss_feed.xml"
    destination_file = "feed"  # New filename without extension
    
    # Copy the source file to the destination with the new name
    os.system(f"cp {source_file} {destination_file}")
    
    print(f"{source_file} copied to {destination_file}")