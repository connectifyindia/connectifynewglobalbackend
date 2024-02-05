import tweepy
import requests
import json
import time
import io
import imghdr
from io import BytesIO

endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/Twiter/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     print(datas)

for data in datas:
      #  image_url=data['image_url']
       image_url="https://connectifyindiasqldb.azurewebsites.net/media/7_Career_Counsel_blog.png"
       response=requests.get(image_url)
       if response.status_code==200:
            image_data = BytesIO(response.content)
            # print(image_data)
          # Determine the file type
            file_type = imghdr.what(None, h=image_data.read(32))
            # print(file_type)
      #  image_url="d:\Local Project\connectifyindia\public\images\Connectify India Homepage 2.png"
       msg=data['content']
    #    f=io.BytesIO(msg)
    #    message=f.read()
     #   print(msg)
       bearer_token=data['bearer_token']
       consumer_key=data['consumer_key']
       consumer_secret=data['consumer_secret']
       access_token=data['access_token']
       access_token_secret=data['access_token_secret']

# V1 Twitter API Authentication
       auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
       auth.set_access_token(access_token,access_token_secret)
       api = tweepy.API(auth, wait_on_rate_limit=True)

# V2 Twitter API Authentication
       client = tweepy.Client(
         bearer_token,
         consumer_key,
         consumer_secret,
         access_token,
         access_token_secret,
         wait_on_rate_limit=True,
        )
       
      #  with open(image_url, "rb") as file:
      #               media_data = file.read()
# Upload image to Twitter. Replace 'filename' your image filename.
       media_id = api.media_upload(filename=file_type).media_id_string

       if len(msg) <= 280:
         client.create_tweet(text=msg,media_ids=[media_id])
         print("Tweeted!")
       else:
         print("we can't perform this bcoz message is too long")