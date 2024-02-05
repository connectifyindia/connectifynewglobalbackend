import requests
import os
import time
import pandas as pd
user_access_token ='EAAEafQqhaTgBO71bLWgSvaAZCrZCXu5ZBoQfutkwfZBH86rce3gO3CACbGqjqZBDeWp4IgKkkxDtMpZBQAyUVB4V42Ptof85DTABvnGZAfO1bt9XPY9ZBJr5rZAjLfhb8PejyVDqo19L3M6OmpRMEqM73kZBWTSPU9oIB6BXr1FUZCdLbv5E36sAnsRa63sXgN9hW7smesse0t3WYF4DSvhPGaiqwe7Tbwk3UNxmxAW8LUZD'
page_id = '109989205132383'
file_path = r"c:/Users/Jitendra.kumar/Desktop/multiple_file.xlsx"
sheet_name = "Sheet1"
dataframe=pd.read_excel(file_path,sheet_name=sheet_name)
# print(dataframe)
n=len(dataframe)
print(n)
for i in range(n):
    description=str(dataframe.description[i])
    # print(description)
    file_url=str(dataframe.file_url[i])
    # file_url=requests.get(file_url)
    # print(file_url)
    video_response = requests.post(
        f'https://graph-video.facebook.com/{page_id}/videos',
        files={'source': open(file_url, 'rb')},
        params={
            'access_token': user_access_token,
            'description':description
        }
    )
    print(video_response.status_code)
    if video_response.status_code == 200:
        video_id = video_response.json()['id']
        post_response = requests.post(
            f'https://graph.facebook.com/{page_id}/feed',
            params={
                'description': description,
                'attached_media[0]': f'{{"media_fbid":"{video_id}"}}',
                'access_token': user_access_token,
            }
        )
        if post_response.status_code == 200:
            print(f'Successfully posted video {video_id}')
            time.sleep(60)
        else:
            print(f'Failed to create post for video {video_id}')
    else:
        print(f'Failed to upload video: {video_response.text}')