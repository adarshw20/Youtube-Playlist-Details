# YouTube Playlist Analyzer

A Python script that fetches and analyzes YouTube playlist data including video statistics, duration, and other metadata.

## Features

- Fetches detailed information about a YouTube playlist
- Calculates total duration of all videos
- Shows view, like, and comment statistics
- Identifies most viewed and most liked videos
- Exports all data to a text file

## Prerequisites

- Python 3.8 or higher
- YouTube Data API v3 key
- Required Python packages (install using `pip install -r requirements.txt`)

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/YouTubePlayTime.git
   cd YouTubePlayTime
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your YouTube API key:
   ```
   YOUTUBE_API_KEY=your_api_key_here
   ```

## How to Get a YouTube API Key

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the YouTube Data API v3
4. Create credentials (API key)
5. Copy the API key and add it to your `.env` file

## Usage

1. Update the `playlist_id` in `app.py` with your desired YouTube playlist ID
2. Run the script:
   ```bash
   python app.py
   ```
3. The script will create a `playlist_details.txt` file with all the information

## Output

The script generates a text file (`playlist_details.txt`) containing:
- Playlist information (title, channel, publish date)
- Statistics (total duration, average video length, etc.)
- Top performing videos
- Complete list of all videos with their details

## Security Note

Never commit your API key to version control. The `.env` file is included in `.gitignore` to prevent accidental commits of sensitive information.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
# Youtube-Playlist-Details
