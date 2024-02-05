import requests
import json
import time

endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/businessconnect/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     n=len(datas)
#     print(datas)
for data in datas:
       image_url=data['image_url']
      #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
     #   print(image_url)
       msg=data['content']
     #   print(msg)
       group_id=data['fb_group_id']
       user_access_token=data['fb_user_access_token']
       
       payload = {'message': msg,'access_token': user_access_token,'url':image_url}
       response = requests.post(f'https://graph.facebook.com/v17.0/{group_id}/photos', data=payload)
       print(response)
       print(response.status_code)
    #   response = requests.post(post_url, data=payload)
       if response.status_code == 200:
        print(f"Image and Message  posted on page {group_id} successfully")
       else:
        print(f"Failed to post on page {group_id}: {response.text}")
# print("All {} Images And Message posted to all Groups Successfully:".format(i + 1))

