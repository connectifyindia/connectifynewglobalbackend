import requests
import os
import time
import pandas as pd
# import io

file_path = r"c:/Users/Jitendra.kumar/Desktop/blogs.xlsx"
sheet_name = "Sheet1"
dataframe = pd.read_excel(file_path, sheet_name=sheet_name)
# print(dataframe.image_url[0])
n = len(dataframe)
# print(n)
title = dataframe["title"].to_list()
link_url = dataframe["link_url"].to_list()
image_urls = dataframe.image_urls
description=dataframe["description"].to_list()
page_id = "109989205132383"
#  access_token="EAADdLTy4LjcBO4vG5fFZBZCQJ8aOCB95W1ZATSey98FYoZAxmdgOM3t04sUVbABgyARJdYTl8ZBLxBQPEnQ0D6jUM0IN5YXaBIk8OPxhn8oDJkyorqosKSWMtjNO5fNB3igKaDHZBUKWvs1oNUgU7uyF580U380mjUItEZAbGJqDR8ZBZBbVIT5e0j3eZASi6GWzG7bi80Um8sYo7XDOZBWEGyqdbrUS2WZCLiV9T2TtkrYZD"
post_url = "https://graph.facebook.com/v17.0/{}/photos".format(page_id)
AccessToken = input("Enter Facebook Access Token=")
# attached_media = []
# for image_url in image_urls:
#     attached_media.append({
#         'media_fbid': 0,  # Use 0 for uploading a new photo
#         'media_url': image_url
#     })
#     print(attached_media)
for i in range(n):
      msg = str(title[i])
      image_url=image_urls[i]

      payload = {'message': msg,'access_token': AccessToken,'url':image_url}
      response = requests.post(post_url, data=payload)
      if response.status_code == 200:
          print("Post published successfully!")
          print(response.json())
      else:
        print("Error publishing post")
        print(response.status_code)
        print(response.text)
      time.sleep(5)
print("All {} Message And Link Sent to Page Legal Aspire Successfully:".format(i + 1))
