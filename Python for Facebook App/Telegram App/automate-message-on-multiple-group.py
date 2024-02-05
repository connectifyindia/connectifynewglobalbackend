
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
       params = {"chat_id": chat_id, "text": msg}

       try:
            response = requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", params=params)
            response.raise_for_status()
            print(f'Message sent to {chat_id} successfully!')
       except requests.exceptions.HTTPError as e:
            print(f"Error sending message: {e}")

   