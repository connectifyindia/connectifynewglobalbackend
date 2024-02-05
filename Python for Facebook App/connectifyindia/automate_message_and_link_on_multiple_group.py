import requests
import json
import time

endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/connectifyindia/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
print(datas)
for data in datas:
      #  image_url=data['image_url']
    #    image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
     #   print(image_url)
       msg=data['content']
       link=data['link_url']
     #   print(msg)
       group_id=data['fb_group_id']
       user_access_token=data['fb_user_access_token']
       payload={
         'message':msg,
         'access_token':user_access_token,
         'link':link
       }
    # print(group_id)
    # graph=fb.GraphAPI(access_token=token)
    # x=graph.put_object(group_id,'feed',data=payload)
       response=requests.post(f'https://graph.facebook.com/v17.0/{group_id}/feed',data=payload)
    # print(x)
       print(response.text)
       time.sleep(5)
# print("All {} Message And Link Sent to All the groups Successfully:".format(i+1))
