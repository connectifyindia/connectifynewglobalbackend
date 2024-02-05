import facebook as fb
groups=['1979851848910110','2264800403755923','2206200109657700']
msg="please Visit Our Blog on Connectify India for Legal,Ngo,Social,Ainaw,Simply Counsel,Business Connect"
link="https://www.connectifyindia.com"
url="https://www.connectifyindia.com/_next/image?url=%2Fimages%2Fsocial%20services.jpeg&w=1920&q=80"
token=input("Enter the Facebook Access Token=")
graph=fb.GraphAPI(access_token=token)
for group in groups:
    x=graph.put_object(group,'photos',message=msg,link=link,url=url)
    print(x)
    print("Message sent Successfully")