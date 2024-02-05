import requests
import os
import time
import pandas as pd
group_file_path = r"D:/ExcelDocs/excel-image/SimplyCounsel.xlsx"
sheet_name = "Sheet2"
groupdataframe=pd.read_excel(group_file_path,sheet_name=sheet_name)
# ***********************************************************************
file_path = r"D:/ExcelDocs/excel-image/SimplyCounsel.xlsx"
sheet_name = "Sheet1"
dataframe = pd.read_excel(file_path, sheet_name=sheet_name)
# print(dataframe.image_url[0])
n = len(dataframe)
# print(n)
message = dataframe["title"].to_list()
image_urls = dataframe.image_urls

# groups=['2264800403755923','2206200109657700','1979851848910110']
# token=input("Enter the Facebook User Access Token=")
# for group_id in groups:
for index, row in groupdataframe.iterrows():
 group_id = row["Group ID"]
 user_access_token = row["User Access Token"]
 for i in range(n):
      msg = str(message[i])
      image_url=image_urls[i]
      payload = {'message': msg,'access_token': user_access_token,'url':image_url}
      response = requests.post(f'https://graph.facebook.com/v17.0/{group_id}/photos', data=payload)
      print(response)
      print(response.status_code)
    #   response = requests.post(post_url, data=payload)
      if response.status_code == 200:
        print(f"Image and Message Number-{i+1} posted on page {group_id} successfully")
      else:
        print(f"Failed to post on page {group_id}: {response.text}")
print("All {} Images And Message posted to all Groups Successfully:".format(i + 1))

