import requests
import json
import time

endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/Linkedln/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     print(datas)
for data in datas:
    #    video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_4.mp4"
       video_url="d:\Local Project\connectifyindia\public\media\short_video2.mp4"
    #    video_url=data['video_url']
       msg=data['content']
     #   print(msg)
       urn_id=data['linkedln_person_urn']
     #   print(page_id)
       access_token=data['access_token']
    #    print(access_token)
       headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
       }
       media_data = {
            "registerUploadRequest": {
                "recipes": ["urn:li:digitalmediaRecipe:feedshare-video"],
                "owner": f"urn:li:person:{urn_id}",
                "serviceRelationships": [
                    {
                        "relationshipType": "OWNER",
                        "identifier": "urn:li:userGeneratedContent",
                    }
                ],
            }
        }

       response1 = requests.post(
            "https://api.linkedin.com/v2/assets?action=registerUpload",
            headers=headers,
            json=media_data,
        )
       print(response1.status_code)
        # print("******************************************************")
       result = json.loads(response1.text)
    #    print("This is result:",result)
       uploadUrl = response1.json()["value"]["uploadMechanism"][
            "com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"
        ]["uploadUrl"]
        # ********************************************************************************************
       headers1 = {
            "Authorization": f"Bearer {access_token}",
            "media-type-family": "VIDEO",
        }
        # print(video_url)
       with open(video_url,"rb") as f:
            data =f.read()

       response = requests.post(uploadUrl, headers=headers1, data=data)
       print(response.status_code)
       print(response.text)
       time.sleep(30)
        # ********************************************************************************************

       if response1.status_code == 200:
            media_urn = response1.json()["value"]["asset"]
            print(media_urn)
       else:
            print("Error uploading media:", response.status_code, response.text)

        # **************************************************************************************************

       SHARE_URL = "https://api.linkedin.com/v2/ugcPosts"

       share_data = {
            "author": f"urn:li:person:{urn_id}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": msg},
                    "shareMediaCategory": "VIDEO",
                    "media": [
                       {
                            "status": "READY",
                            "description": {"text": "Center stage!"},
                            "media": media_urn,
                            "title": {"text": "LinkedIn Talent Connect 2023"},
                        }
                    ],
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
        }

       response = requests.post(SHARE_URL, headers=headers, json=share_data)
       print(response.text)
       if response.status_code == 201:
            print("Successfully posted on LinkedIn.")
       else:
            print("Error posting on LinkedIn:", response.status_code, response.text)