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
     #   document_url="https://create.microsoft.com/en-us/launch-app?wdTpl=TM67429532&app=WORD&fallbackUrl=https%3A%2F%2Fwww.microsoft365.com%2Flaunch%2FWord%3Fms.url%3Dtemplates.Word.new%26templateId%3DTM67429532%26omkt%3Den-us"
      #  document="c:\Users\Jitendra.kumar\Desktop\Linkedlin\New Text Document.txt"
     #   with open("c:/Users/Jitendra.kumar/Desktop/Linkedlin/New Text Document.txt","rb") as file:
     #       document_url=file.read()
     #       print(document_url)
       document_message_params={
            'chat_id':chat_id,
            'document':document_url,
            'caption':msg
            } 
       
       try:
        # Send the video message
            response =requests.post(f'https://api.telegram.org/bot{bot_token}/sendDocument',params=document_message_params)
            response.raise_for_status()
            print(f'Document Sent {chat_id} Successfully!')
       except requests.exceptions.HTTPError as e:
            print(f'Error sending Document:{e}')

