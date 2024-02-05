import tweepy
import requests
import json
import time

endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/Twiter/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     print(datas)
for data in datas:
       msg=data['content']
     #   print(msg)
    #    bearer_token=data['bearer_token']
    #    print(bearer_token)
       consumer_key=data['consumer_key']
    #    print(consumer_key)
       consumer_secret=data['consumer_secret']
    #    print(consumer_secret)
       access_token=data['access_token']
    #    print(access_token)
       access_token_secret=data['access_token_secret']
    #    print(access_token_secret)

# V1 Twitter API Authentication
       auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
       auth.set_access_token(access_token,access_token_secret)
       api = tweepy.API(auth, wait_on_rate_limit=True)

       client = tweepy.Client(
          consumer_key=consumer_key, consumer_secret=consumer_secret,
          access_token=access_token, access_token_secret=access_token_secret
       )
    #    msg = '''Labour Day to honor the hardworking men and women.Welcome to Connectify India, your one-stop platform for all your career counseling, legal services, social service, and business needs.'''
# client.create_tweet(text=text)
       if len(msg)<=280:
         client.create_tweet(text=msg)
         print("Message Tweeted Successfully")
       else:
        print("Tweet is too long.Please shorten your message.")