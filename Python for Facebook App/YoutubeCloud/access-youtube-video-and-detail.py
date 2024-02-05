import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Set your API key and credentials JSON file path
api_key = 'YOUR_API_KEY'
credentials_path = 'path/to/your/credentials.json'

# Initialize the YouTube Data API client
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

# Define the video ID you want to retrieve information for
video_id = 'VIDEO_ID'

try:
    # Request video details
    video_request = youtube.videos().list(
        part='snippet',
        id=video_id
    )
    video_response = video_request.execute()

    # Print video details
    video_info = video_response['items'][0]['snippet']
    print(f'Title: {video_info["title"]}')
    print(f'Description: {video_info["description"]}')
    print(f'Published At: {video_info["publishedAt"]}')
    print(f'Channel Name: {video_info["channelTitle"]}')

except googleapiclient.errors.HttpError as e:
    print(f'An error occurred: {e}')
