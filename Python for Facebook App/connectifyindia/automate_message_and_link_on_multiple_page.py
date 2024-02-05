import requests
import json
import time

endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/connectifyindia/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     print(datas)
for data in datas:
       msg=data['content']
     #   print(msg)
       page_id=data['fb_page_id']
     #   print(page_id)
       access_token=data['fb_page_access_token']
      #  print(access_token)
       link=data['link_url']
    #    print(link)
       payload={
         'message':msg,
         'access_token':access_token,
         'link':link
        }
       response=requests.post('https://graph.facebook.com/{}/feed'.format(page_id),data=payload)
       print(response.text)
       print(f'Message And Link Sent to Page id: {page_id}')
       time.sleep(5)



