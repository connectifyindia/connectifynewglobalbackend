import requests
import json
import time
endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/whatsapps/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     n=len(datas)
# print(datas)
#     image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
for data in datas:
       msg=data['content']
      #  print(msg)
      #  print("*******************************************************")
       phone_number_id=data['phone_number_id']
      #  print(phone_number_id)
      #  WhatsApp_Business_Account_ID=data['WhatsApp_Business_Account_ID']
       auth_token=data['auth_token']
      #  print(auth_token)
      #  print("*******************************************************")
       recepient_number=data['recepient_number']
      #  print(recepient_number)
      #  print("*******************************************************")
       city_name=data['city_name']
       video_url=data['video_url']
      #  video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_4.mp4"
       post_url=f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"

    # Construct the payload
       payload = {
         "recipient_type": "individual",
         "to": recepient_number,
         "type": "video",
         "video": {
         "link": video_url
         },
         "messaging_product": "whatsapp",
}
# Headers with authentication token
       headers = {
         "Authorization": f"Bearer {auth_token}",
         "Content-Type": "application/json"
        }

# Send the POST request
       response = requests.post(post_url, json=payload, headers=headers)
       print(response)

       if response.status_code == 200:
         print("Message sent successfully!")
         print(response.text)
       else:
         print("Failed to send message:", response.text)

