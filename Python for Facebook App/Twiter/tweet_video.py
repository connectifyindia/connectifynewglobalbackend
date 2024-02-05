import tweepy
# bearer_token = r'AAAAAAAAAAAAAAAAAAAAAH9fpgEAAAAAf4Mb2LKZ6QiDV9II4UYpbqI2NVs%3DbBjY6vDVJY1cAAh9epGb2z0nUqNf8VUfuzJDBPA2ZOa5Zf7hWf'
# consumer_key = 'U4QVLIy6zEjVC5azlOB2Ie4nk'
# consumer_secret = 'Uif26DJwRjMc7PExMkjTABEGUyK4FYCVLJ4CZ9AU21C1hSWSWv'
# access_token = '1552707819606265856-72Fng0Y9ayPRuUqjIxWNZXJTeHkeyh'
# access_token_secret = '85CBh5C4kpFiQRmEvnaCXbf2hkzxVQqOnoss49jfvKUyF'

bearer_token = r"AAAAAAAAAAAAAAAAAAAAAH9fpgEAAAAArO1%2FYddCUR19mtdtGxNvcYJjfJ4%3DANaxcGUEFmFxHYGhdK54mwv5H8L0gkp6u5d1dWGPh49nfhAeyW"
consumer_key = "ydmQsSDb4SfGaHuWUuXM1eF4H"
consumer_secret = "H2iJNU2cewOGz9OFPfWuGhvtgIbCGs3vInuoVo2Tm1PtaDfqBX"
access_token = "1552707819606265856-B76PrNygiLnbNE5DJvc1QaUp5XSRyh"
access_token_secret = "s6SNhWvHyHtBEfpGjzRVkZvM61NTe95W1waC9Cn47rMs9"

# V1 Twitter API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
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

# Upload image to Twitter. Replace 'filename' your image filename.
media_id = api.media_upload(filename="d:\Global Project\connectifyindia\public\media\short_video.mp4").media_id_string
print(media_id)

# Text to be Tweeted
message ="""
https://www.connectifyindia.com
Connectify Business Global Pvt Ltd
About The Company
Welcome to Connectify India, your one-stop platform for all your career counseling, legal services, social service, and business needs.
"""
if len(message) <= 280:
    client.create_tweet(text=message, media_ids=[media_id])
    print("Tweeted!")
    # Tweet the message if it's within the character limit
    
else:
    print("Tweet is too long.Please shorten your message.")
    
# Send Tweet with Text and media ID
