# Kurakahani Podcast Extraction and RSS Feed Generation

This project aims to automate the extraction of audio content from the "Kurakahani" podcast videos on YouTube, convert them to audio files, and generate an RSS feed for easy distribution. The audio files and the RSS feed are made available on this GitHub repository.

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

The "Kurakahani" podcast presents engaging discussions and valuable insights on various topics. This project aims to make these discussions more accessible by providing audio versions of the podcast episodes along with an RSS feed that listeners can subscribe to.

**Check out the [Kurakahani YouTube Channel](https://www.youtube.com/@KuraKahaniPodcast) for the original video content.**


## Features

- Automatic extraction of audio content from "Kurakahani" podcast videos.
- Conversion of video episodes to audio files.
- Generation of an RSS feed for podcast distribution.

## Usage

This project automatically extracts audio content from the "Kurakahani" podcast videos, converts them to audio files, and generates an RSS feed for easy distribution. You don't need to run any scripts manually to benefit from this project.

## How It Works

Behind the scenes, this project employs a combination of automation, scripting, and the YouTube Data API. Here's how it works:

1. **Automation Script**: An automation script periodically checks for new podcast videos on the [Kurakahani YouTube Channel](https://www.youtube.com/@KuraKahaniPodcast).

2. **Audio Conversion**: When a new video is detected, the script uses a tool to download and convert the video's audio into MP3 format.

3. **RSS Feed Generation**: The metadata (title, description, etc.) of the video is extracted using the YouTube Data API. An RSS feed is then automatically generated using this metadata and the link to the converted audio file.

4. **GitHub Action**: The entire process is automated through a GitHub Action workflow. It runs the automation script and ensures that the latest audio files and RSS feed are available on this repository: [https://github.com/ChandanShakya/Kurakahani](https://github.com/ChandanShakya/Kurakahani).

You don't need to run any scripts yourself to access the audio content or RSS feed. Simply visit the repository linked above to access the content.

## Prerequisites

- Access to the [Kurakahani YouTube Channel](https://www.youtube.com/@KuraKahaniPodcast).
- A web browser to access the content on the GitHub repository.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, suggestions, or collaboration opportunities, please feel free to reach out to:

Chandan Shakya

ZXY-CC-3ag13@pm.me

