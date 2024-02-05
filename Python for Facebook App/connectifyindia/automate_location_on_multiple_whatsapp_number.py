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
# message=dataframe['message'].to_list()
city_name=dataframe['city_name'].to_list()
address=dataframe['address'].to_list()
longitude=dataframe['longitude'].to_list()
latitude=dataframe['latitude'].to_list()
post_url=f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"
for i in range(n):
    # whatsapp_user
    whatsapp_number=str(whatsapp_number[i])
    city=city_name[i]
    address=address[i]
    longitude=longitude[i]
    latitude=latitude[i]

    # Construct the payload
    payload = {
      "recipient_type": "individual",
      "to": whatsapp_number,
      "type": "location",
      "location": {
         "longitude":longitude,
         "latitude":latitude,
         "name": city,
         "address": address
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

    if response.status_code == 200:
     print("Message sent successfully!")
     print(response.text)
    else:
     print("Failed to send message:", response.text)

