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
       http_url=data['image_url']
       response = requests.head(http_url, allow_redirects=True)
       image_url = response.url
       print(image_url)
    #    image_url = 'https://www.esamskriti.com/essays/docfile/8_6742.jpg'  # Replace with the actual URL of your image
    #    image_url="d:/Local Project/connectifyindia/public/images/3 Legal Aspire Homepage.png"
       msg=data['content']
     #   print(msg)
       urn_id=data['linkedln_person_urn']
       group_urn_id=data['linkedln_group_urn']
       access_token=data['access_token']
       MEDIA_UPLOAD_URL = 'https://api.linkedin.com/v2/assets?action=registerUpload'
# ACCESS_TOKEN="AQUhISHZpNwr4vkEEdAviYnhPFpLwAxTedZ0s4wjXd2gvTSaJvPcAN8mzyLjkTJ9F9sEtKGVwBl8v4y5ivPZkG6cOfuiEWD5k6zJwJzqRbB13Kl1QRBEPPXzei4HIvGSHFltVNQtdGC6rySY0wax3ZI8PY9usis9hNLffMS4Ihg-mFs_-yC8BBezzKM_ZfHJwHOyV5c5lmQIoGq73-zpi3vQ0Uzp4xEJYdsUYoTayVvabyEiHfDczfjw9k-4l-ZmwjEABS-J8yQKFhBtF04dMj4m-8maekHybpaY3PO9VnoLHCQdUhrteEEIt3XmsJLryOY_lUTrZ6rpmUImHDhPbGmRUCLFug"

       headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

       media_data = {
            'registerUploadRequest': {
                'recipes': ['urn:li:digitalmediaRecipe:feedshare-image'],
                'owner': f'urn:li:person:{urn_id}',
                'serviceRelationships': [
                    {
                        'relationshipType': 'OWNER',
                        'identifier': 'urn:li:userGeneratedContent'
                    }
                ]
            }
        }

       response1 = requests.post(MEDIA_UPLOAD_URL, headers=headers, json=media_data)
       print(response1.status_code)
       print("******************************************************")
       result=json.loads(response1.text)
        # print(result)
       uploadUrl=response1.json()['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest'][
                'uploadUrl']
# print(uploadUrl)

# ********************************************************************************************
       headers1 = {
            'Authorization': f'Bearer {access_token}',
            'media-type-family': 'STILLIMAGE'
        }
    #    payload={
    #         'submitted-image-url':image_url
    #    }



    #    with open(image_url,'rb') as f:
    #         data = f.read()

       response = requests.post(uploadUrl,headers=headers1,data=image_url)
       print(response.status_code)
       print(response.text)
        # ********************************************************************************************

       if response1.status_code == 200:
            media_urn= response1.json()['value']['asset']
            # print(media_urn)
       else:
            print('Error uploading media:', response.status_code, response.text)


        # **************************************************************************************************

       SHARE_URL = 'https://api.linkedin.com/v2/ugcPosts'

       share_data = {
            "author": f"urn:li:person:{urn_id}",
            'containerEntity': f'urn:li:group:{group_urn_id}',
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": "Ganesha, the son of Lord Shiva and Devi Parvati, is revered by the general public and known by a variety of names, including Sumukha, Ekadanta, Kapila, Gajakarna, Lambodara, Vikath, Vidhnanashaka, Vinayaka, Bhalchandra, and Gajanana. Lord Ganesha's paintings appear incredibly alluring and captivating. Millions of people have shown love and devotion to the adorable little elephant-headed boy-like physique throughout history. While every manifestation of Lord Ganesha paintings awakens our imaginations and brings us unparalleled joy, each one also carries profound spiritual symbolism."
                    },
                    "shareMediaCategory": "IMAGE",
                    "media": [
                        {
                            "status": "READY",
                            "description": {
                                "text": "Ganesha, the son of Lord Shiva and Devi Parvati, is revered by the general public and known by a variety of names, including Sumukha, Ekadanta, Kapila, Gajakarna, Lambodara, Vikath, Vidhnanashaka, Vinayaka, Bhalchandra, and Gajanana. Lord Ganesha's paintings appear incredibly alluring and captivating."
                            },
                            "media":media_urn,
                            "title": {
                                "text": "Lord Ganesha Painting"
                            }
                        }
                    ]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "CONTAINER"
            }
        }
        # print(media_urn)
       response = requests.post(SHARE_URL, headers=headers, json=share_data)
       print(response.text)
       if response.status_code == 201:
            print('Successfully posted on LinkedIn.')
       else:
            print('Error posting on LinkedIn:', response.status_code, response.text)

