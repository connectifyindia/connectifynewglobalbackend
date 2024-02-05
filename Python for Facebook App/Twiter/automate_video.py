import tweepy
import requests
import json
import time
import os
from requests_oauthlib import OAuth1Session

endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/Twiter/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     print(datas)
for data in datas:
       media_file=data['video_url'] 
    #    print(media_file)
    #    media_file="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_4.mp4"    
       msg=data['content']
     #   print(msg)
       bearer_token=data['bearer_token']
       consumer_key=data['consumer_key']
       consumer_secret=data['consumer_secret']
       access_token=data['access_token']
       access_token_secret=data['access_token_secret']

       media_file = "d:\Global Project\connectifyindia\public\media\short_video.mp4"


# Media file to upload

# Set up OAuth 1.0a session
       twitter_auth =OAuth1Session(
          client_key=consumer_key,
          client_secret=consumer_secret,
          resource_owner_key=access_token,
          resource_owner_secret=access_token_secret
       )

# V1 Twitter API Authentication
       auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
       auth.set_access_token(access_token, access_token_secret)
       api = tweepy.API(auth, wait_on_rate_limit=True)
       client = tweepy.Client(
            bearer_token,
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret,
            wait_on_rate_limit=True,
        )
       # Step 1: Initialize media upload
       media_upload_url = "https://upload.twitter.com/1.1/media/upload.json"
       media_init_params = {
            "command": "INIT",
            "media_type": "video/mp4",  # Change to "video/mp4" for videos
            "total_bytes": os.path.getsize(media_file)
        }
       media_init_response = twitter_auth.post(
            media_upload_url, params=media_init_params
        )
    #    print(media_init_response.status_code)
       if media_init_response.status_code!=202:
            print(f"Error initializing media upload: {media_init_response.status_code}")
       else:
            media_id = json.loads(media_init_response.text).get("media_id_string")

            if media_id is None:
                print("Error: 'media_id_string' not found in the response.")
            else:
                # Step 2: Append media
                media_append_url = "https://upload.twitter.com/1.1/media/upload.json"
                media_append_params = {
                    "command": "APPEND",
                    "media_id": media_id,
                    "segment_index": 0
                }

                with open(media_file, "rb") as file:
                    media_data = file.read()

                media_append_response = twitter_auth.post(
                    media_append_url, params=media_append_params, data=media_file
                )

                if media_append_response.status_code !=400:
                    print(f"Error appending media: {media_append_response.status_code}")
                else:
                    # Step 3: Finalize media
                    media_finalize_url = "https://upload.twitter.com/1.1/media/upload.json"
                    media_finalize_params = {
                        "command": "FINALIZE",
                        "media_id": media_id,
                    }

                    media_finalize_response = twitter_auth.post(
                        media_finalize_url, params=media_finalize_params
                    )

                    if media_finalize_response.status_code != 400:
                        print(f"Error finalizing media: {media_finalize_response.status_code}")
                    else:
                        # Step 4: Tweet with the uploaded media
                        tweet_text = "Check out this media!"
                        tweet_url = "https://api.twitter.com/1.1/statuses/update.json"
                        tweet_params = {
                            "status": tweet_text,
                            "media_ids": [media_id],
                        }

                        tweet_response = twitter_auth.post(
                            tweet_url, params=tweet_params
                        )

                        if tweet_response.status_code == 200:
                            print("Media uploaded and tweeted successfully!")
                        else:
                            print(f"Error tweeting: {tweet_response.status_code} - {tweet_response.text}")
