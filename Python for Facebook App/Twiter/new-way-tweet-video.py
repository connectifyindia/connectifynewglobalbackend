import requests
import base64

# API v2 endpoint for uploading media
media_upload_url = "https://api.twitter.com/2/media/upload"

# Your Twitter API v2 Bearer Token
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAH9fpgEAAAAArO1%2FYddCUR19mtdtGxNvcYJjfJ4%3DANaxcGUEFmFxHYGhdK54mwv5H8L0gkp6u5d1dWGPh49nfhAeyW'

# Authenticate and prepare headers
headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'multipart/form-data',
}

# Specify the video file path
video_file_path = 'd:\Global Project\connectifyindia\public\media\short_video.mp4'

# Read the video file as binary
with open(video_file_path, 'rb') as video_file:
    video_data = video_file.read()

# Encode video data as base64
video_base64 = base64.b64encode(video_data).decode('utf-8')

# Create a request payload
data = {
    'media_type': 'video/mp4',
    'media_category': 'tweet_video',
    'media_data': video_base64,
}

# Upload the video
response = requests.post(media_upload_url, headers=headers, json=data)

if response.status_code == 201:
    media_id = response.json()['data']['media_id']
    print(f"Video uploaded with media ID: {media_id}")

    # Now, you can create a tweet and attach the uploaded video using the media ID
    # Refer to the Twitter API v2 documentation for how to create tweets with media.
else:
    print(f"Error uploading video: {response.status_code}, {response.text}")
