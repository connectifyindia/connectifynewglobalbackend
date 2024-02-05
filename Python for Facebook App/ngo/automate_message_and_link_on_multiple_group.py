import requests
# import facebook as fb
import os
import time
import pandas as pd
page_file_path = r"D:/ExcelDocs/excel-link/NGO.xlsx"
sheet_name = "Sheet2"
groupdataframe=pd.read_excel(page_file_path,sheet_name=sheet_name)

#**************************************************************************
file_path = r"D:/ExcelDocs/excel-link/NGO.xlsx"
sheet_name = "Sheet1"
dataframe=pd.read_excel(file_path,sheet_name=sheet_name)
n=len(dataframe)
print(n)
title=dataframe['title'].to_list()
url=dataframe['url'].to_list()
# groups=['2264800403755923','2206200109657700','1979851848910110']
# token=input("Enter the Facebook User Access Token=")
# for group_id in groups:
for index, row in groupdataframe.iterrows():
 group_id = row["Group ID"]
 user_access_token = row["User Access Token"]
 for i in range(n):
    msg=str(title[i])
    link=str(url[i])
    # print(group)
    payload={
    'message':msg,
    'access_token':user_access_token,
    'link':link
    }
    # print(group_id)
    # graph=fb.GraphAPI(access_token=token)
    # x=graph.put_object(group_id,'feed',data=payload)
    response=requests.post(f'https://graph.facebook.com/v17.0/{group_id}/feed',data=payload)
    # print(x)
    print(response.text)
    time.sleep(5)
print("All {} Message And Link Sent to All the groups Successfully:".format(i+1))
