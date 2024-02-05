import requests
import json
import time
endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/Linkedln/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     n=len(datas)
#     print(datas)
for data in datas:
      #  image_url=data['image_url']

       http_url=data['image_url']
       response = requests.head(http_url,allow_redirects=True)
       image_url = response.url
      #  print(image_url)

      #  image_url="d:/Local Project/connectifyindia/public/images/business 1.jpeg"
       msg=data['content']
     #   print(msg)
       urn_id=data['linkedln_person_urn']
     #   print(page_id)
       access_token=data['access_token']
      #  print(access_token)
      #  image_url = 'http://www.esamskriti.com/essays/docfile/8_6742.jpg'  # Replace with the actual URL of your image
       MEDIA_UPLOAD_URL ='https://api.linkedin.com/v2/assets?action=registerUpload'
      # ACCESS_TOKEN="AQUhISHZpNwr4vkEEdAviYnhPFpLwAxTedZ0s4wjXd2gvTSaJvPcAN8mzyLjkTJ9F9sEtKGVwBl8v4y5ivPZkG6cOfuiEWD5k6zJwJzqRbB13Kl1QRBEPPXzei4HIvGSHFltVNQtdGC6rySY0wax3ZI8PY9usis9hNLffMS4Ihg-mFs_-yC8BBezzKM_ZfHJwHOyV5c5lmQIoGq73-zpi3vQ0Uzp4xEJYdsUYoTayVvabyEiHfDczfjw9k-4l-ZmwjEABS-J8yQKFhBtF04dMj4m-8maekHybpaY3PO9VnoLHCQdUhrteEEIt3XmsJLryOY_lUTrZ6rpmUImHDhPbGmRUCLFug"

       headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        "X-Restli-Protocol-Version": "2.0.0"
        }

       media_data = {
        'registerUploadRequest': {
        'owner':f'urn:li:person:{urn_id}',
        'recipes': ['urn:li:digitalmediaRecipe:feedshare-image'],
        'serviceRelationships': [
            {
                'relationshipType': 'OWNER',
                'identifier': 'urn:li:userGeneratedContent'
            }
            ]
           }
        }
      

       response1 = requests.post(MEDIA_UPLOAD_URL,headers=headers,json=media_data)
       print(response1.status_code)
       print("******************************************************")
       result=json.loads(response1.text)
       print(result)
       uploadUrl=response1.json()['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest'][
        'uploadUrl']
      #  print(uploadUrl)

# ********************************************************************************************
       headers1 = {
          'Authorization': f'Bearer {access_token}',
          "media-type-family": "STILLIMAGE",
          "Content-Type": "image/png"
        }
      #  with open(image_url,'rb') as f:
      #    data = f.read()
       response = requests.post(uploadUrl,headers=headers1,data=image_url)
       print(response.status_code)
       print(response.text)
# ********************************************************************************************

       if response1.status_code == 200:
          media_urn= response1.json()['value']['asset']
          print(media_urn)
       else:
           print('Error uploading media:', response.status_code, response.text)


# **************************************************************************************************

       SHARE_URL = 'https://api.linkedin.com/v2/ugcPosts'

       share_data = {
         "author": f"urn:li:person:{urn_id}",
         "lifecycleState": "PUBLISHED",
         "specificContent": {
         "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text":msg
            },
            "shareMediaCategory": "IMAGE",
            "media": [
                {
                    "status": "READY",
                    "description": {
                        "text":msg 
                    },
                    "media":media_urn,
                    "title": {
                        "text": "create linkdln profile"
                    }
                }
            ]
           }
          },
          "visibility": {
          "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
          }
          }
# print(media_urn)
       response = requests.post(SHARE_URL, headers=headers, json=share_data)
       print(response.status_code)
       print(response.text)
       if response.status_code == 201:
          print('Successfully posted on LinkedIn.')
       else:
          print('Error posting on LinkedIn:', response.status_code, response.text) 