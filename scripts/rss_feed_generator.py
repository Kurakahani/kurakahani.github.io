def generate_rss_entry(metadata):
    rss_entry = f"""
    <item>
        <title>{metadata['title']}</title>
        <description>{metadata['description']}</description>
        <enclosure url="https://raw.githubusercontent.com/ChandanShakya/Kurakahani/main/{metadata['audio_url']}" length="1" type="audio/mpeg"/>
        <author>{metadata['author']}</author>
        <pubDate>{metadata['published_date']}</pubDate>
        <guid>https://raw.githubusercontent.com/ChandanShakya/Kurakahani/main/{metadata['audio_url']}</guid>
        <itunes:author>{metadata['author']}</itunes:author>
        <itunes:explicit>no</itunes:explicit>
        <itunes:image href="https://raw.githubusercontent.com/ChandanShakya/Kurakahani/main/{metadata['image']}.jpg"/>
    </item>
    """
    return rss_entry


def update_rss_feed(metadata):
    rss_header = """
        <?xml version="1.0" encoding="UTF-8"?>
        <rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
        <channel>
            <title>Kurakahani Podcast</title>
            <link>https://www.youtube.com/@KuraKahaniPodcast</link>
            <language>ne</language>
            <itunes:author>Prabin Buddhacharya</itunes:author>
            <itunes:category text="Entertainment"/>
            <itunes:image href="https://raw.githubusercontent.com/ChandanShakya/Kurakahani/main/images/logo.jpg"/>
            <description>We are Kurakahani Podcast channel. We do podcast with different people of different background. Trying to hear and share the story of them.
            We are team of three individuals with different interest but the talking and sharing of different idea bought us together and here we are to share and hear the story of us and our friends guest that shows up on the podcast.
            Kurakahani is a platform to share the feelings, ideas, gossip and many more.
            Support us by anyway possible to grow.
            Thank you</description>
            <itunes:explicit>no</itunes:explicit>
        """
    rss_footer = """
        </channel>
        </rss>
        """
    rss_content = rss_header + generate_rss_entry(metadata) + rss_footer

    # Check if the file exists, and create it if not
    try:
        with open("rss_feed.xml", "x", encoding="utf-8") as f:
            f.write(rss_content)
    except FileExistsError:
        # File already exists, so append to it
        with open("rss_feed.xml", "a", encoding="utf-8") as f:
            f.write(generate_rss_entry(metadata))
