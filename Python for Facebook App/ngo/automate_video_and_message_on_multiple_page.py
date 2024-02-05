import requests
endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/ainaw/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     print(datas)

for data in datas:
       msg=data['content']
       video_url=data['video_url']
       page_id=data['fb_page_id']
       access_token=data['fb_page_access_token']
       video_response = requests.post(f'https://graph-video.facebook.com/{page_id}/videos',
              files={'source': video_url},
               #  files={'source': open('d:\Global Project\connectifyindia\public\media\short_video1.mp4', 'rb')},

         params={
            'access_token':access_token,
            'description':msg
            }
            )

       if video_response.status_code == 200:
           video_id = video_response.json()['id']
           post_response = requests.post(
            f'https://graph.facebook.com/{page_id}/feed',
           params={
                'description':msg,
                'attached_media[0]': f'{{"media_fbid":"{video_id}"}}',
                'access_token': access_token,
            }
           )
       if video_response.status_code == 200:
            print(f"Posted to Facebook Page {page_id} successfully.")
       else:
            print(f"Failed to post on page {page_id}: {video_response.text}")
