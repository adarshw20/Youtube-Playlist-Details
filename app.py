import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import isodate
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv('YOUTUBE_API_KEY')
if not api_key:
    raise ValueError("Please set the YOUTUBE_API_KEY in the .env file")

def format_duration(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def format_number(num):
    if num >= 1000000:
        return f"{num/1000000:.1f}M"
    elif num >= 1000:
        return f"{num/1000:.1f}K"
    return str(num)

# Initialize YouTube API
try:
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # Get playlist ID from user input
    playlist_id = input("Enter YouTube Playlist ID: ").strip()
    if not playlist_id:
        print("Error: Playlist ID cannot be empty")
        exit(1)
        
except Exception as e:
    print(f"Error initializing YouTube API: {e}")
    exit(1)

try:
    # Get playlist details
    playlist_request = youtube.playlists().list(
        part='snippet,contentDetails',
        id=playlist_id
    )
    playlist_response = playlist_request.execute()
except Exception as e:
    print(f"An error occurred while fetching playlist details: {e}")
    print("This might be due to an invalid Playlist ID, an incorrect API key, or a network issue.")
    print("Please check your .env file and the provided Playlist ID.")
    exit(1)

if not playlist_response['items']:
    print("Playlist not found!")
    exit()

playlist = playlist_response['items'][0]
playlist_title = playlist['snippet']['title']
channel_title = playlist['snippet']['channelTitle']

# Handle timestamp with or without microseconds
published_at_str = playlist['snippet']['publishedAt']
try:
    published_at = datetime.strptime(published_at_str, '%Y-%m-%dT%H:%M:%SZ').strftime('%B %d, %Y')
except ValueError:
    published_at = datetime.strptime(published_at_str, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%B %d, %Y')

total_videos = playlist['contentDetails']['itemCount']

print("="*60)
print(f"PLAYLIST: {playlist_title}")
print(f"Channel: {channel_title}")
print(f"Published: {published_at}")
print(f"Total Videos: {total_videos}")
print("="*60 + "\n")

# Initialize variables
total_seconds = 0
video_count = 0
view_count = 0
like_count = 0
comment_count = 0
videos = []
next_page_token = None

# Fetch all videos in the playlist
while True:
    pl_request = youtube.playlistItems().list(
        part='snippet,contentDetails',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=next_page_token
    )
    pl_response = pl_request.execute()
    video_ids = [item['contentDetails']['videoId'] for item in pl_response['items']]
    
    # Get video details
    vid_request = youtube.videos().list(
        part='contentDetails,statistics,snippet',
        id=','.join(video_ids)
    )
    vid_response = vid_request.execute()

    # Process each video
    for item in vid_response['items']:
        video_count += 1
        snippet = item['snippet']
        stats = item['statistics']
        
        # Calculate duration
        duration = isodate.parse_duration(item['contentDetails']['duration']).total_seconds()
        total_seconds += duration
        
        # Get view, like, and comment counts (handle potential missing fields)
        views = int(stats.get('viewCount', 0))
        likes = int(stats.get('likeCount', 0))
        comments = int(stats.get('commentCount', 0))
        
        view_count += views
        like_count += likes
        comment_count += comments
        
        # Store video details
        videos.append({
            'title': snippet['title'],
            'duration': duration,
            'views': views,
            'likes': likes,
            'published_at': snippet['publishedAt'],
            'url': f"https://youtu.be/{item['id']}"
        })
    
    next_page_token = pl_response.get('nextPageToken')
    if not next_page_token:
        break

# Calculate statistics
average_duration = total_seconds / video_count if video_count > 0 else 0
most_viewed = max(videos, key=lambda x: x['views']) if videos else None
most_liked = max(videos, key=lambda x: x['likes']) if videos else None

# Print overall statistics
print("📊 PLAYLIST STATISTICS")
print("-" * 60)
print(f"• Total Duration: {format_duration(total_seconds)}")
print(f"• Average Video Length: {format_duration(average_duration)}")
print(f"• Total Views: {format_number(view_count)}")
print(f"• Total Likes: {format_number(like_count)}")
print(f"• Total Comments: {format_number(comment_count)}")
print("\n🏆 TOP VIDEOS")
print("-" * 60)
if most_viewed:
    print(f"👀 Most Viewed: {most_viewed['title']} ({format_number(most_viewed['views'])} views)")
    print(f"   {most_viewed['url']}")
if most_liked and most_liked != most_viewed:
    print(f"❤️  Most Liked: {most_liked['title']} ({format_number(most_liked['likes'])} likes)")
    print(f"   {most_liked['url']}")

# Save all details to a file
with open('playlist_details.txt', 'w', encoding='utf-8') as f:
    # Write playlist header
    f.write("="*60 + "\n")
    f.write(f"PLAYLIST: {playlist_title}\n")
    f.write(f"Channel: {channel_title}\n")
    f.write(f"Published: {published_at}\n")
    f.write(f"Total Videos: {total_videos}\n")
    f.write("="*60 + "\n\n")
    
    # Write statistics
    f.write("📊 PLAYLIST STATISTICS\n")
    f.write("-" * 60 + "\n")
    f.write(f"• Total Duration: {format_duration(total_seconds)}\n")
    f.write(f"• Average Video Length: {format_duration(average_duration)}\n")
    f.write(f"• Total Views: {format_number(view_count)}\n")
    f.write(f"• Total Likes: {format_number(like_count)}\n")
    f.write(f"• Total Comments: {format_number(comment_count)}\n\n")
    
    # Write top videos
    f.write("🏆 TOP VIDEOS\n")
    f.write("-" * 60 + "\n")
    if most_viewed:
        f.write(f"👀 Most Viewed: {most_viewed['title']} ({format_number(most_viewed['views'])} views)\n")
        f.write(f"   {most_viewed['url']}\n")
    if most_liked and most_liked != most_viewed:
        f.write(f"❤️  Most Liked: {most_liked['title']} ({format_number(most_liked['likes'])} likes)\n")
        f.write(f"   {most_liked['url']}\n")
    
    # Write all videos
    f.write("\n📺 ALL VIDEOS\n")
    f.write("-" * 60 + "\n")
    for idx, video in enumerate(videos, 1):
        # Handle potential datetime format variations
        try:
            pub_date = datetime.strptime(video['published_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%b %d, %Y')
        except ValueError:
            pub_date = datetime.strptime(video['published_at'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%b %d, %Y')
            
        f.write(f"\n{idx}. {video['title']}\n")
        f.write(f"   ⏱️  {format_duration(video['duration'])} | 👁️  {format_number(video['views'])} views | ❤️  {format_number(video['likes'])}\n")
        f.write(f"   📅 {pub_date}\n")
        f.write(f"   🔗 {video['url']}")

print("\n✅ Playlist details have been saved to 'playlist_details.txt' in the current directory.")
