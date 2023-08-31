# Kurakahani Podcast Extraction, RSS Feed Generation and Website Creation

This project aims to automate the extraction of audio content from the "Kurakahani" podcast videos on YouTube, convert them to audio files, generate an RSS feed, and finally create a website at [kurakahani.github.io](https://kurakahani.github.io) where users can easily access and explore the podcast's episodes.

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Prerequisites](#prerequisites)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About the Project

The "Kurakahani" podcast offers engaging discussions and valuable insights on various topics. This project enhances accessibility by providing audio versions of podcast episodes, along with an RSS feed and a dedicated website where listeners can explore the content.

**Check out the [Kurakahani YouTube Channel](https://www.youtube.com/@KuraKahaniPodcast) for the original video content.**


## Features

- Automatic extraction of audio content from "Kurakahani" podcast videos.
- Conversion of video episodes to audio files.
- Generation of an RSS feed for podcast distribution.
- Creation of a dedicated website at [kurakahani.github.io](https://kurakahani.github.io) for easy access to podcast episodes.

## Usage

This project automatically extracts audio content from "Kurakahani" podcast videos, converts them to audio files, generates an RSS feed, and creates a dedicated website. You can explore the podcast's episodes and access the content on the [kurakahani.github.io](https://kurakahani.github.io) website.

## How It Works

Behind the scenes, this project employs a combination of automation, scripting, and the YouTube Data API. Here's how it works:

1. **Automation Script**: An automation script periodically checks for new podcast videos on the [Kurakahani YouTube Channel](https://www.youtube.com/@KuraKahaniPodcast).

2. **Audio Conversion**: When a new video is detected, the script uses a tool to download and convert the video's audio into M4A format.

3. **RSS Feed Generation**: The metadata (title, description, etc.) of the video is extracted using the YouTube Data API. An RSS feed is then automatically generated using this metadata and the link to the converted audio file.

4. Website Creation: The project also generates a dedicated website at [kurakahani.github.io](https://kurakahani.github.io), where users can explore and access the podcast's episodes.

All these processes are automated through a GitHub Action workflow, ensuring that the latest audio files, RSS feed, and website are available at [kurakahani.github.io](https://kurakahani.github.io).

## Prerequisites

- Access to the [Kurakahani YouTube Channel](https://www.youtube.com/@KuraKahaniPodcast).
- A web browser to explore and access the content on the [kurakahani.github.io](https://kurakahani.github.io) website.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## License
This project is licensed under [the MIT License](https://github.com/Kurakahani/Kurakahani.github.io/blob/main/LICENSE).

## Contact
For any inquiries, suggestions, or collaboration opportunities, please feel free to reach out to:

Kurakahani Podcast

kurakahani@gmail.com

