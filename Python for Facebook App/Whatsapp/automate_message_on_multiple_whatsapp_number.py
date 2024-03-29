import requests
import json
import time
endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/whatsapps/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
# print(datas)
for data in datas:
       msg=data['content']
       print(msg)
       phone_number_id=data['phone_number_id']
       print(phone_number_id)
      #  WhatsApp_Business_Account_ID=data['WhatsApp_Business_Account_ID']
       auth_token=data['auth_token']
       print(auth_token)
       recepient_number=data['recepient_number']
       print(recepient_number)
       city_name=data['city_name']
       post_url=f"https://graph.facebook.com/v18.0/{phone_number_id}/messages"

      # Construct the payload
       payload = {
         "messaging_product": "whatsapp",
         "recipient_type": "individual",
         "to": recepient_number,
         "type": "template",
        #  "text": {
        #    "preview_url": False,
        #    "body": msg
        #  },
         
         "template": {
             "name": "hello_world",
             "language": {
                "code": "en_US"
              }
    }
}

# Headers with authentication token
       headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
        }

# Send the POST request
       response = requests.post(post_url,json=payload,headers=headers)

       if response.status_code == 200:
         print("Message sent successfully!")
         print(response.text)
       else:
         print("Failed to send message:", response.text)

