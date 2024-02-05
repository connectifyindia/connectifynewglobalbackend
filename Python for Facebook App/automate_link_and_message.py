import requests
import os
import time
import pandas as pd
file_path = r"c:/Users/Jitendra.kumar\Documents/top5Url.xlsx"
sheet_name = "Sheet2"
dataframe=pd.read_excel(file_path,sheet_name=sheet_name)
n=len(dataframe)
print(n)
title=dataframe['title'].to_list()
url=dataframe['url'].to_list()
page_id="102046439274468"
# access_token="EAAOBuKAMl60BOyTHJv4BnSZBDYOX4rgF80BNdJpQl1FdZCER2txTfRkZCe4SegEJkFl2hwAUJs7NUxt8VTCOcnmi3Po9YAQO7zzjedUKfrx58NTeJOuIQ1lZCx4tFuHKW46gMp8EyWrXqZAQeSvcmMyTLRMNVZCjnTftRXk1Xf8ewoP8UuQJwk3PgDdgaJtFXzIf0m5N6bv9YxuzAZD"
post_url='https://graph.facebook.com/{}/feed'.format(page_id)
AccessToken=input("Enter Facebook Access Token=")
for i in range(n):
    msg=str(title[i])
    link=str(url[i])
    payload={
    'message':msg,
    'access_token':AccessToken,
    'link':link
    }
    response=requests.post(post_url,data=payload)
    print(response.text)
    time.sleep(5)
print("All {} Message And Link Sent to Page Legal Aspire Successfully:".format(i+1))



