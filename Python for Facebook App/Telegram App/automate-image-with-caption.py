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
       image_url=data['image_url']
      #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
     #   print(image_url)
       msg=data['content']
     #   print(msg)
       chat_id=data['chat_id']
      #  print(chat_id)
       bot_token=data['bot_token']
       image_params = {
       'chat_id': chat_id,
       'photo':image_url,
       'caption':msg
       }
       try:
        response = requests.post(f'https://api.telegram.org/bot{bot_token}/sendPhoto', params=image_params)
        response.raise_for_status()
        print('Image sent successfully!')
       except requests.exceptions.HTTPError as e:
        print(f'Error sending image: {e}')




