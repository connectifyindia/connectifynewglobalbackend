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
      #  print(image_url)
      #  image_url="http://www.esamskriti.com/essays/docfile/8_6742.jpg"
     #   print(image_url)
       msg=data['content']
     #   print(msg)
       chat_id=data['chat_id']
      #  print(chat_id)
       bot_token=data['bot_token']
      #  print(bot_token)
      #  document_url=data['document']
    #    document_url=data['document']
      #  document_url="https://create.microsoft.com/en-us/launch-app?wdTpl=TM67429532&app=WORD&fallbackUrl=https%3A%2F%2Fwww.microsoft365.com%2Flaunch%2FWord%3Fms.url%3Dtemplates.Word.new%26templateId%3DTM67429532%26omkt%3Den-us"
       image_params = {
       'chat_id': chat_id,
       'photo':image_url,
       'caption':msg
      }
       upload_url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'

       try:
         response = requests.post(upload_url,params=image_params)
         response.raise_for_status()
         print('Message and Image sent to {chat_id} successfully')

       except requests.exceptions.HTTPError as e:
        print(f'Error sending image: {e}')