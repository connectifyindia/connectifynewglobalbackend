import requests
import time
import json

# ... Your access token, account ID, and video file path ...
access_token='EAAEafQqhaTgBO4IviG7d9G1wb8OJsAdJCYsXpHnY2ZBvAKPZCSqVStZA6cbCZBKgAvZCV7tp2IDCnNv1Oy54T4woSLFQVvKGVAqYudUV6xqruMys7tTQToarpKYoKOZCGM0dbKZBT1vwpCuPeqb4y5Ct6TX17CdrKdiolmu3t4YV6IvMtqBpz4PYxpwomyRMC49jOnS8yorbAF7sZBlHMXBResbj3qaYhtFwIiZC3V1CRbrWXudU9jK6CDHEVUXy29S2PRx6WZCP1oSkgZD'
ig_user_id='17841408718588683'
video_url='https://connectifyindiasqldb.azurewebsites.net/y2mate.com_-_Connectify_India_Company_Service_details_360p.mp4'
# Step 1: Upload the video

post_url=f'https://graph.facebook.com/v17.0/{ig_user_id}/media'
payload={
    'caption':'connectify India',
    'video_url':video_url,
    'media_type':'VIDEO',
    'access_token':access_token
}

response=requests.post(post_url,data=payload)
response_json = response.json()
print(response_json)
print("*********************")
creation_id = response_json.get('id')

# Step 2: Check media status

status_url = f"https://graph.facebook.com/v17.0/{creation_id}?fields=status&access_token={access_token}"
while True:
    status_response = requests.get(status_url)

    try:
        status_data = status_response.json()
        media_status = status_data.get('status')
    except json.JSONDecodeError:
        print("Failed to decode JSON response. Retrying...")
        time.sleep(10)  # Wait for 10 seconds before retrying
        continue

    if media_status == 'READY':
        break
    elif media_status == 'PROCESSING':
        print("Media is still processing. Waiting...")
        time.sleep(10)  # Wait for 10 seconds before checking again
        break
    else:
        print("Media status:", media_status)
        # break

# Step 3: Publish the video
        publish_url = f"https://graph.facebook.com/v17.0/{ig_user_id}/media_publish"
        publish_data = {
         'creation_id': creation_id,
         'access_token':access_token
        }

        publish_response = requests.post(publish_url, data=publish_data)

        if publish_response.status_code == 200:
          print("Video successfully published!")
          break
        else:
          print("Failed to publish the video:")
