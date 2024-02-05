import requests
import json
import time

endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/instagram/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     n=len(datas)
#     print(datas)
#     image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
for data in datas:
       image_url=data['image_url']
      #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
     #   print(image_url)
       msg=data['content']
     #   print(msg)
       page_id=data['fb_page_id']
     #   print(page_id)
       access_token=data['fb_page_access_token']
       print(access_token)
       ig_user_id=data['instagram_user_id']
      #  print(ig_user_id)
       payload={
        'caption':msg,
        'access_token':access_token,
        'image_url':image_url
       }
       response=requests.post('https://graph.facebook.com/v17.0/{}/media'.format(ig_user_id),data=payload)
       print(response.text)
       print("Media Uploaded Successfully")
       results=json.loads(response.text)
       if 'id' in results:
        creation_id=results['id']
        second_url='https://graph.facebook.com/v17.0/{}/media_publish'.format(ig_user_id)
        second_payload={
           'creation_id':creation_id,
           'access_token':access_token
        }
        response=requests.post(second_url,data=second_payload)
        if response.status_code==200:
           print("image published to instagram")
        else:
           print("image posting is not possible")



