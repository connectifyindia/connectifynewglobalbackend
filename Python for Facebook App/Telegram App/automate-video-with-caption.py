import requests
import json
import time
endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/telegrams/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
# n=len(datas)
# print(datas)
for data in datas:
       video_url=data['video_url']
      #  video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_4.mp4"
     #   print(image_url)
       msg=data['content']
     #   print(msg)
       chat_id=data['chat_id']
      #  print(chat_id)
       bot_token=data['bot_token']
       video_message_params = {
       'chat_id': chat_id,
       'video': video_url,
       'caption':msg
       }
       try:
        # Send the video message
         response = requests.post(f'https://api.telegram.org/bot{bot_token}/sendVideo', params=video_message_params)
         response.raise_for_status()
         print('Video sent successfully!')
       except requests.exceptions.HTTPError as e:
         print(f'Error sending video: {e}')