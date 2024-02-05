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
       image_url=data['image_url']
     #   image_url=image_url.replace("http://", "https://")
     #   print(image_url)
      #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
     #   print(image_url)
       msg=data['content']
     #   print(msg)
       phone_number_id=data['phone_number_id']
      #  WhatsApp_Business_Account_ID=data['WhatsApp_Business_Account_ID']
     #   print(page_id)
       auth_token=data['auth_token']
      #  print(auth_token)
       recepient_number=data['recepient_number']
      #  post_url=f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"
       post_url=f"https://graph.facebook.com/v17.0/109187762280261/messages"
       payload = {
        "recipient_type": "individual",
        # "to": recepient_number,
        "to": 917519526081,
        "type": "image",
        "image": {
        "link": image_url
        },
        "messaging_product": "whatsapp",
}
# Headers with authentication token
       headers = {
         "Authorization": f"Bearer {auth_token}",
         "Content-Type": "application/json"
         }
       

# Send the POST request
       response = requests.post(post_url,json=payload,headers=headers)
       print(response.text)
       if response.status_code == 200:
         print("Message sent successfully!")
         print(response.text)
       else:
        print("Failed to send message:", response.text)
