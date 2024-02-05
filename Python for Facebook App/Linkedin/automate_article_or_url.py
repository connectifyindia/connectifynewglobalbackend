import requests
import json
import time

endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/Linkedln/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     print(datas)
for data in datas:
    #    thumbnail_url="http://img.freepik.com/premium-psd/business-youtube-thumbnail-design-template_475351-263.jpg"
       originalUrl=data['link_url']
       thumbnail_url=data['thumbnail_url']
    #    print(thumbnail_url)
     #   print(image_url)
       msg=data['content']
     #   print(msg)
       urn_id=data['linkedln_person_urn']
     #   print(page_id)
       access_token=data['access_token']
    #    print(access_token)
       POST_URL = 'https://api.linkedin.com/v2/ugcPosts'
# text="""
# The example below creates a simple text Share on LinkedIn.Notice the visibility is set to PUBLIC, where anyone on the LinkedIn Platform can view this share.
# """
       headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'x-li-format': 'json'
        }

       post_data = {
            'author': f'urn:li:person:{urn_id}',
            'lifecycleState':'PUBLISHED',
            'visibility': {
                'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'
            },
            'specificContent': {
                'com.linkedin.ugc.ShareContent': {
                    'shareCommentary': {
                        'text': msg
                    },
                    "shareMediaCategory": "ARTICLE",
                    "media": [
                        {
                            "status": "READY",
                            "description": {
                                "text": "Official LinkedIn Blog - Your source for insights and information about LinkedIn."
                            },
                            "originalUrl":originalUrl,
                            "title": {
                                "text": "Official LinkedIn Blog"
                            },
                            "thumbnails":[{
                            "url":thumbnail_url
                    }]
                        }
                    ]
                }
            }
        }

       response = requests.post(POST_URL,headers=headers,json=post_data)
       if response.status_code == 201:
            print('Successfully posted on LinkedIn.',response.text)
       else:
            print('Error posting on LinkedIn:',response.status_code,response.text)

        

        