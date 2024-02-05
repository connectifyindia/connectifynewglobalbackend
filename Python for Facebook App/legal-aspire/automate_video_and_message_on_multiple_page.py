import requests
endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/legalaspire/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
# #     print(datas)
# # video_url="https://dsqqu7oxq6o1v.cloudfront.net/preview-309NO7Sx4HuQI.mp4"

for data in datas:
       msg=data['content']
       http_url=data['video_url']
       response = requests.head(http_url, allow_redirects=True)
       video_url = response.url
#      #   print(video_url)
       # video_url="http://connectifyindiasqldb.azurewebsites.net/media/Connectify_India_Company_Profile.mp4"
       page_id=data['fb_page_id']
       access_token=data['fb_page_access_token']
       video_response = requests.post(f'https://graph-video.facebook.com/v18.0/{page_id}/videos',
          #     files={
          #          'file_url':video_url
          #          },
#                #  files={'source': open('d:\Global Project\connectifyindia\public\media\short_video1.mp4', 'rb')},

         params={
            'access_token':access_token,
            'description':msg,
            'file_url':video_url
            }
            )

#        if video_response.status_code == 200:
#            video_id = video_response.json()['id']
#            post_response = requests.post(
#             f'https://graph.facebook.com/{page_id}/feed',
#            params={
#                 'description':msg,
#                 'attached_media[0]': f'{{"media_fbid":"{video_id}"}}',
#                 'access_token': access_token,
#             }
#            )
       if video_response.status_code == 200:
            print(f"Posted to Facebook Page {page_id} successfully.")
       else:
            print(f"Failed to post on page {page_id}: {video_response.text}")



