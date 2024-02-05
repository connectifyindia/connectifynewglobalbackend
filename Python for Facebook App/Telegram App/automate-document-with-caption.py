import requests
import json
import time
endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/telegrams/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
# print(datas)
for data in datas:
       msg=data['content']
     #   print(msg)
       chat_id=data['chat_id']
      #  print(chat_id)
       bot_token=data['bot_token']
      #  print(bot_token)
       document_url=data['document']
       document_message_params = {
        'chat_id': chat_id,
        'document': document_url,
        'caption':msg
        }
      
       try:
        # Send the video message
         response = requests.post(f'https://api.telegram.org/bot{bot_token}/sendDocument', params=document_message_params)
         response.raise_for_status()
         print('Document sent successfully!')

       except requests.exceptions.HTTPError as e:
         print(f'Error sending Document: {e}')

# Replace 'YOUR_BOT_TOKEN' with the API token you obtained from BotFather
# bot_token = '6621902852:AAFB3sgYDSAzWMGm-sUQNIsd7V-3mOdks9c'
# Replace 'RECIPIENT_ID' with the user or group chat ID where you want to send the message
# recipient_id = '1168845505'
# document_url = 'https://kamarajcollege.ac.in/Department/BCA/III%20Year/Core%2039%20-%20Operating%20Systems.pdf'

# URL for sending a video
# video_message_url = f'https://api.telegram.org/bot{bot_token}/sendDocument'

# Set parameters for the video message
# try:
#     # Send the video file
#     with open("d:\Global Project\connectifyindia\public\media\short_video.mp4", "rb") as video_file:
#         response = requests.post(video_message_url, params=video_message_params, files={'video': video_file})
#         response.raise_for_status()
#         print('Video sent successfully!')

# except requests.exceptions.HTTPError as e:
#     print(f'Error sending video: {e}')