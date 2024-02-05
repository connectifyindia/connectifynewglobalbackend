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
     #   image_url=data['image_url']
     #   image_url=image_url.replace("http://", "https://")
     #   print(image_url)
    #    image_url="d:/Local Project/connectifyindia/public/images/business 1.jpeg"
     #   print(image_url)
       msg=data['content']
     #   print(msg)
       urn_id=data['linkedln_person_urn']
     #   print(page_id)
       access_token=data['access_token']
    #    print(access_token)
# ACCESS_TOKEN='AQX6U1u7agaLAPj3-MDfIk8YGlZpSJP1cH3DsgtBYpo1nrVcUxswmUzC-3QqcXBGLfOWM3geThEC8qKKZYpLl_52Tusq36wFq1KoL8ve_Gyfq-EGN3_v8A2ddc1ZegPoT2MBNM1zx9tcvTV5zCY-sQozP3SO7ZjKXe1cOBbxXLlFp2Zc2io5RebdblbGMXsdmZxaLv2TPe3Xj-lxUe8GzE2jAL1zxk1sKAXfc3BtIAZjnAIxl5Ue4pAwuRsE-T2vmp0Y7tX53r4fI3mTJB_BKRXBcj4Ug4RMh_s79M6XvU7amES4j2SuInAQs6AuUesBjXhD4cBaMsu49ofcHLSP-BEtbVVVhQ'
       POST_URL ='https://api.linkedin.com/v2/ugcPosts'
# text="""
# The example below creates a simple text Share on LinkedIn. Notice the visibility is set to PUBLIC, where anyone on the LinkedIn Platform can view this share.
# """
       headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'x-li-format': 'json'
        }

       post_data = {
            'author': f'urn:li:person:{urn_id}',
            'lifecycleState': 'PUBLISHED',
            'visibility': {
                'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'
            },
            'specificContent': {
                'com.linkedin.ugc.ShareContent': {
                    'shareCommentary': {
                        'text':msg
                    },
                    'shareMediaCategory': 'NONE'
                }
            }
        }

       response = requests.post(POST_URL,headers=headers,json=post_data)
       if response.status_code == 201:
            print('Successfully posted on LinkedIn.',response.text)
       else:
            print('Error posting on LinkedIn:', response.status_code, response.text)
