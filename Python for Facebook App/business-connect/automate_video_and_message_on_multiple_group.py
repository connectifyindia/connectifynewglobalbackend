import requests
import os
import time
import pandas as pd

group_file_path = r"D:/ExcelDocs/excel-video/BusinessConnect.xlsx"
sheet_name = "Sheet2"
groupdataframe=pd.read_excel(group_file_path,sheet_name=sheet_name)
# ***********************************************************************
file_path = r"D:/ExcelDocs/excel-video/BusinessConnect.xlsx"
sheet_name = "Sheet1"
dataframe=pd.read_excel(file_path,sheet_name=sheet_name)
# print(dataframe)
n=len(dataframe)
print(n)
# groups=['2264800403755923','2206200109657700','1979851848910110']
# token=input("Enter the Facebook User Access Token=")
# for group_id in groups:
for index, row in groupdataframe.iterrows():
 group_id = row["Group ID"]
 user_access_token = row["User Access Token"]
 for i in range(n):
    message=str(dataframe.description[i])
    # print(description)
    file_url=str(dataframe.file_url[i])
    # file_url=requests.get(file_url)
    # print(file_url)
    video_response = requests.post(
        f'https://graph-video.facebook.com/v17.0/6459575797457516/videos',
        files={'source': open(file_url, 'rb')},
        params={
            'access_token':user_access_token
        }
    )
    print(video_response.status_code)
    if video_response.status_code == 200:
        video_id = video_response.json()['id']
        post_response = requests.post(
            f'https://graph.facebook.com/v17.0/{group_id}/feed',
            params={
                'description': message,
                'attached_media[0]': f'{{"media_fbid":"{video_id}"}}',
                'access_token':user_access_token,
            }
        )
        if post_response.status_code == 200:
            print(f'Successfully {i+1} video posted on id: {video_id}')
            time.sleep(5)
        else:
            print(f'Failed to create post for video {video_id}')
    else:
        print(f'Failed to upload video: {video_response.text}')

