import requests
import json
import time

endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/Linkedln/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     print(datas)
for data in datas:
    #    thumbnail_url="https://img.freepik.com/premium-psd/business-youtube-thumbnail-design-template_475351-263.jpg"
    #    video_url="d:\Local Project\connectifyindia\public\media\short_video2.mp4"
    #    video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_4.mp4"
       msg=data['content']
     #   print(msg)
       thumbnail_url=data['thumbnail_url']
       video_url=data['video_url']
       urn_id=data['linkedln_person_urn']
       group_urn_id=data['linkedln_group_urn']
       access_token=data['access_token']
       MEDIA_UPLOAD_URL = 'https://api.linkedin.com/v2/assets?action=registerUpload'
       headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
       media_data = {
            'registerUploadRequest': {
                'recipes': ['urn:li:digitalmediaRecipe:feedshare-video'],
                'owner': f'urn:li:person:{urn_id}',
                'serviceRelationships': [
                    {
                        'relationshipType': 'OWNER',
                        'identifier': 'urn:li:userGeneratedContent'
                    }
                ]
            }
        }

       response1 = requests.post(MEDIA_UPLOAD_URL,headers=headers,json=media_data)
    #    print(response1.status_code)
    #    print("******************************************************")
       result=json.loads(response1.text)
    #    print(result)
       uploadUrl=response1.json()['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
        # ********************************************************************************************
       headers1 = {
            'Authorization': f'Bearer {access_token}',
            "media-type-family": "VIDEO"
        }

    #    with open(video_url, 'rb') as f:
    #         data = f.read()

       response = requests.post(uploadUrl,headers=headers1,data=video_url)
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
            'containerEntity':f'urn:li:group:{group_urn_id}',
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": "Feeling inspired after meeting so many talented individuals at this year's conference. #talentconnect"
                    },
                    "shareMediaCategory": "VIDEO",
                    "media": [
                        {
                            "status": "READY",
                            "description": {
                                "text":msg
                            },
                            "media":media_urn,
                            "title": {
                                "text": "LinkedIn Talent Connect 2023"
                            },
                            "thumbnails":[{
                                "url":thumbnail_url
                            }]
                        }
                    ]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "CONTAINER"
            }
        }

       response = requests.post(SHARE_URL, headers=headers, json=share_data)
       print(response.text)
       if response.status_code == 201:
            print('Successfully posted on LinkedIn.')
       else:
            print('Error posting on LinkedIn:', response.status_code, response.text)

