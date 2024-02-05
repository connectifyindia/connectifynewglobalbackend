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
       thumbnail_url=data['thumbnail_url']
       originalUrl=data['link_url']
     #   print(image_url)
       msg=data['content']
     #   print(msg)
       urn_id=data['linkedln_person_urn']
       group_urn_id=data['linkedln_group_urn']
       access_token=data['access_token']
    #    print(access_token)
       POST_URL = 'https://api.linkedin.com/v2/ugcPosts'
# text="""
# Welcome to Connectify India, your one-stop platform for all your career counseling, legal services, social service, and business needs. Our four verticals work towards connecting students, teachers, advocates, law students, interns, consumers, NGOs, and business owners across India. We are dedicated to providing the best career counseling services for students and professionals, legal services for consumers in need, connecting social service organizations to help society, and connecting businesses with consumers to make informed decisions. For now we are Working in india, but also targeting the global market for future. Join us and let us help you make the best choices for your future.
# """
       headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'x-li-format': 'json'
        }

       post_data = {
            'author': f'urn:li:person:{urn_id}',
            'containerEntity':f'urn:li:group:{group_urn_id}',
            'lifecycleState': 'PUBLISHED',
            'visibility': {
                'com.linkedin.ugc.MemberNetworkVisibility': 'CONTAINER'
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
                                "text": "Welcome to Connectify India, your one-stop platform for all your career counseling, legal services, social service, and business needs. Our four verticals work towards connecting students, teachers, advocates, law students, interns, consumers, NGOs, and business owners across India."
                            },
                            "originalUrl": originalUrl,
                            "title": {
                                "text": "Connectify India Company Service details"
                            },
                            "thumbnails":[{
                                "url":thumbnail_url
                            }]
                        }
                    ]
                }
            }
        }

       response = requests.post(POST_URL, headers=headers, json=post_data)
       if response.status_code == 201:
            print('Successfully posted on LinkedIn.')
       else:
            print('Error posting on LinkedIn:', response.status_code, response.text)