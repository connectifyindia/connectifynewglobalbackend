import requests
import json
import time

endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/ainaw/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     print(datas)
for data in datas:
       image_url=data['image_url']
      #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
     #   print(image_url)
       msg=data['content']
     #   print(msg)
       page_id=data['fb_page_id']
     #   print(page_id)
       access_token=data['fb_page_access_token']
      #  print(access_token)
       payload = {
            'message':msg,
            'access_token':access_token,
            'url':image_url,
           }
       response = requests.post(f'https://graph.facebook.com/v17.0/{page_id}/photos', data=payload)
       if response.status_code == 200:
            print(f"Image and Message posted on page {page_id} successfully")
       else:
            print(f"Failed to post on page {page_id}: {response.text}") 