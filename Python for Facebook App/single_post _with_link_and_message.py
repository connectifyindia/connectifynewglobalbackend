import requests
page_id="102046439274468"
# access_token="EAAOBuKAMl60BOyTHJv4BnSZBDYOX4rgF80BNdJpQl1FdZCER2txTfRkZCe4SegEJkFl2hwAUJs7NUxt8VTCOcnmi3Po9YAQO7zzjedUKfrx58NTeJOuIQ1lZCx4tFuHKW46gMp8EyWrXqZAQeSvcmMyTLRMNVZCjnTftRXk1Xf8ewoP8UuQJwk3PgDdgaJtFXzIf0m5N6bv9YxuzAZD"
post_url='https://graph.facebook.com/{}/feed'.format(page_id)
AccessToken=input("Enter Facebook Access Token=")
msg=input("Enter the Message=")
link=input("Enter The Link=")
payload={
    'message':msg,
    'access_token':AccessToken,
    'link':link
}
response=requests.post(post_url,data=payload)
print(response.text)
print("Message Sent Successfully")


