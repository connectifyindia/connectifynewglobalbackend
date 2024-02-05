import requests
import json
import time

def publish_image(video_url,msg,access_token,ig_user_id):
       payload={
         'caption':msg,
         'access_token':access_token,
         'media_type': 'VIDEO',
         'video_url':video_url
        }
       response=requests.post('https://graph.facebook.com/v17.0/{}/media'.format(ig_user_id),data=payload)
       print(response.text)
       print("Media Uploaded Successfully")
       time.sleep(30)
       results=json.loads(response.text)
       if 'id' in results:
         creation_id=results['id']
         status_url = f"https://graph.facebook.com/v17.0/{creation_id}?fields=status&access_token={access_token}"
         
         while True:
           status_response = requests.get(status_url)

           try:
             status_data = status_response.json()
             media_status = status_data.get('status')
           except json.JSONDecodeError:
             print("Failed to decode JSON response. Retrying...")
             time.sleep(10)  # Wait for 10 seconds before retrying
             continue
           
           second_url='https://graph.facebook.com/v17.0/{}/media_publish'.format(ig_user_id)
           second_payload={
              'creation_id':creation_id,
              'access_token':access_token
             }
           response=requests.post(second_url,data=second_payload)
           if response.status_code == 200:
              print("Video successfully published!")
              break
           else:
              print("Failed to publish the video:")
endpoint="https://connectifyglobalbackend.azurewebsites.net/social-media/api/instagram/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
for data in datas:
       video_url=data['video_url']
      #  video_url="https://dsqqu7oxq6o1v.cloudfront.net/preview-309NO7Sx4HuQI.mp4"
     #   print(image_url)
       msg=data['content']
     #   print(msg)
       
      #  page_id=data['fb_page_id']
     #   print(page_id)
       access_token=data['fb_page_access_token']
       ig_user_id=data['instagram_user_id']
# access_token="EAAEafQqhaTgBO1W0EZAel2goii8CYCIUy4ysfWQ733u9uoxcK42Efeo7nOrPntztXD5HsfrT8zdQVdpfvTzb0Jl4hZCgmeRHWjBmhz5YfBeZAGbKShcAwciyxTUghSrlIUXBMRMsE2XkduuVsZATbZBfMg5DhVlo81RZAflLInTlOy3hzzSCPpOvliUMBesMfUcldkCYHTpwFUwCFqGTRyD1ttVTMUMZAYEOsVHOLUX7vwguP0GHmLZCiWjDQVkJIro5rYzuHOPXMRIZD"
publish_image(video_url,msg,access_token,ig_user_id)





