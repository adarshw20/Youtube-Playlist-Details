# Youtube Playlist Details

A powerful Python script to analyze and extract detailed statistics from any public YouTube playlist. Get comprehensive insights about video durations, view counts, likes, and more with just a few commands.

## ✨ Features

- 📊 **Playlist Statistics**: Total duration, average video length, and more
- 🎯 **Video Analysis**: View counts, like ratios, and engagement metrics
- 🏆 **Top Performers**: Identify most viewed and most liked videos
- 📝 **Detailed Reports**: Export all data to a well-formatted text file
- 🔄 **Pagination Support**: Handles playlists of any size

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- YouTube Data API v3 key ([Get one here](https://console.cloud.google.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Youtube-Playlist-Details.git
   cd Youtube-Playlist-Details
   ```

2. **Set up a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**
   - Create a `.env` file in the project root
   - Add your YouTube API key:
     ```
     YOUTUBE_API_KEY=your_api_key_here
     ```

## 🛠️ Usage

1. **Edit the script** (optional)
   - Open `app.py` and modify the `playlist_id` variable to analyze a different playlist

2. **Run the analyzer**
   ```bash
   python app.py
   ```

3. **View the results**
   - Check `playlist_details.txt` for the complete analysis

## 📊 Example Output

The script generates a detailed report including:
- Playlist metadata (title, channel, video count)
- Aggregate statistics (total views, likes, comments)
- Performance metrics (average duration, engagement rates)
- Complete video list with individual stats

## 🔒 Security

- Your API key is stored in `.env` which is ignored by Git
- Never commit sensitive information to version control
- Consider restricting your API key usage in the Google Cloud Console

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute:
1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 Notes

- The script handles YouTube API rate limits automatically
- For large playlists, processing may take some time
- Ensure your API key has sufficient quota for the YouTube Data API v3

---

Built with ❤️ by [Your Name]
