import requests
import json
import time
# pages = [
#     {"page_id": "109989205132383", "access_token":"EAAEafQqhaTgBO6jjtHGEmD3VZAtcLRRtTLosielyvGwxgwfZAzjcqXWla0DZA8ZBHYou2qIigs0fR4AOlAsHvguNb20S750PlpRxIxxPQiC9sPVkXWP4roznjT5CPNBZBzQF2e77ZBFsXv77nGMCQxBAYhaICg1BT41x68y6ZCMGAZBnkz00PtWLuC8uTTP8t8meDn5zi7wbuIFxxSkZD"},
#     {"page_id": "350000959091406", "access_token":"EAAEafQqhaTgBO7TcY1raciEOkQgubVIQWm3NfEPQo5x6Rv6dlFBOZAUO3qoOxUtuuTUe4urzZAzJ3ilEf6S0eEhULfzxWd35bjB3SDXUOu4AsISvC8sGJW0cfiZAIPXnMxkL4DbaXns2mf332QzuLfSmcA3EXMlR0eYs7z5Xo7P2kRTGcRKG7OZAOT1JNdXri8l7iAINNrXfMxIR"}
# ]
endpoint="http://127.0.0.1:5463/social-media/api/simplycounsel/"
results=requests.get(endpoint)
dic_data=results.json()
datas=dic_data['results']
#     n=len(datas)
#     print(datas)
#     image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
for data in datas:
     #   image_url=data['image_url']
     #   image_url=image_url.replace("http://", "https://")
     #   print(image_url)
       image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
     #   print(image_url)
       msg=data['content']
     #   print(msg)
       page_id=data['fb_page_id']
     #   print(page_id)
       access_token=data['fb_page_access_token']
     #   print(access_token)
     #   print("--------------------------------------------------------------------------------")
      #  for data in pages:
      #      page_id=data['page_id']
      #      page_access_token=data['access_token']

       payload = {
            'message':msg,
            'access_token':access_token,
            'url':image_url,
           }
       response = requests.post(f'https://graph.facebook.com/v17.0/{page_id}/photos', data=payload)
       if response.status_code == 200:
            print(f"Image and Message posted on page {page_id} successfully")
       else:
            print(f"Failed to post on page {page_id}: {response.text}") 
          #  if response.status_code == 200:
          #     return HttpResponse(f"Post Posted to Facebook Page {page_id} successfully.")
          # #   return render(request,"/templates/home.html",context={'page_id':page_id})
          #  else:
          #   return HttpResponse(f"Failed to post on page {page_id}: {response.text}")