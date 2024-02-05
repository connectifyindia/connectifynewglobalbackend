import requests
import os
import time
import pandas as pd
phone_number_id=input("Enter Phone number id=")
auth_token=input("Enter Auth Token=")
file_path = r"c:/Users/Jitendra.kumar/Desktop/whatsapp_cloud_api.xlsx"
sheet_name = "Sheet1"
dataframe=pd.read_excel(file_path,sheet_name=sheet_name)
n=len(dataframe)
print(n)
# whatsapp_user_name=dataframe['whatsapp_user_name'].to_list()
whatsapp_number=dataframe['whatsapp_user_number'].to_list()

post_url=f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"
message=dataframe['message'].to_list()
for i in range(n):
    # whatsapp_user_name=whatsapp_user_name[i]
    whatsapp_number=str(whatsapp_number[i])
    message=message[i]

    # Construct the payload
    payload = {
      "recipient_type": "individual",
      "to": whatsapp_number,
      "type": "text",
      "text": {
        "body": message
       },
      "messaging_product": "whatsapp",
    # "template": {
    #      "name": "hello_world", "language": { "code": "en_US" }
    #        }
}

# Headers with authentication token
    headers = {
     "Authorization": f"Bearer {auth_token}",
     "Content-Type": "application/json"
    }

# Send the POST request
    response = requests.post(post_url, json=payload, headers=headers)

    if response.status_code == 200:
     print("Message sent successfully!")
     print(response.text)
    else:
     print("Failed to send message:", response.text)

