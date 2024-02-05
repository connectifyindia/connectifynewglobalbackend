import requests
import json
import time
def publish_image(image_url,access_token):
    # access_token=input("Enter Access Token=")
    ig_user_id="17841431996866861"
    # image_url="http://connectifyindiasqldb.azurewebsites.net/Connectify_India_company_profile.png"
    post_url='https://graph.facebook.com/v17.0/{}/media'.format(ig_user_id)
    payload={
        'image_url':image_url,
        'caption':"instagram post using Graph API",
        'access_token':access_token
    }
    response=requests.post(post_url,data=payload)
    print(response.text)
    print("Media Uploaded Successfully")
    results=json.loads(response.text)
    if 'id' in results:
        creation_id=results['id']
        second_url='https://graph.facebook.com/v17.0/{}/media_publish'.format(ig_user_id)
        second_payload={
           'creation_id':creation_id,
           'access_token':access_token
        }
        response=requests.post(second_url,data=second_payload)
        if response.status_code==200:
           print("image published to instagram")
        else:
           print("image posting is not possible")

access_token="EAAEafQqhaTgBOZCJnkxfNsHxa6qhJfHpE5kuIqLAbSqpkSY6aCqyWKOAnpA8SeWEr9TciQZBrLvd8IOHhuHoor3nliTY2eZCTFYHGbmAK3DKMP2ZAJ5fKzLqsC553ky9AiTM0xKO4tih23FwGvZArFWIwwN7tNhQZCod7ERvfv9y6MJK1ZAt7pKoTVHgukSGTLRZCiCSRwXRGZCmHOkEZD"
image_url1='https://img.freepik.com/free-vector/lord-ganpati-ganesh-chaturthi-beautiful-green-leaf-holiday-card-background_1035-24526.jpg?size=626&ext=jpg&ga=GA1.1.195888180.1703141872&semt=sph'
publish_image(image_url1,access_token)
time.sleep(20)
image_url2='http://connectifyindiasqldb.azurewebsites.net/career_counselling.jpeg'
publish_image(image_url2,access_token)


