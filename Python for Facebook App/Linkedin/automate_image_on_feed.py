import requests
# Your LinkedIn API endpoint for sharing
share_endpoint = "https://api.linkedin.com/v2/shares"

# Your LinkedIn access token
access_token = "AQXcA5GDthFlDWPrpL_AD4yelLwPKjNEsJGW6Gq-iYexSk8ROgJdpAT9kGDIcyJ1Cbki-2Ow7rWhd4ILOjmU8geRDyxyqpE4HOVWvfjp3woHiAwPEs1Bd73SWrmM7CfTlCbuHEzSf01sSzJKairMBwu1UlhOnQScMqNFiCbNYXHG5bEqx5OVbuBwTw8ENfY87pQxY-GiEvPFV5uTw4ovwP_lxk_n3PeHsqTlGNx8epg5mZT03hm3m_qZPYEG_Dr1sZaGwfsAbDdixcOtQBGzbHNLCfNKEczLoCXgsiCUhhHv1w13xheNjpDPuZgEFwcPQLaLWyVeI5odqi9IEOxf7grZnU7eZw"

# Your image URL on the server
image_url = "http://connectifyindiasqldb.azurewebsites.net/media/2_Career_Counsel_Homepage.png"

# Create the share payload
share_payload = {
     "owner": "urn:li:person:yVc_muusPt",
     "subject": "Your image title goes here.",
     "text": {
        "text": "Your image description goes here."
    },
    "content": {
        "contentEntities": [
            {
                "entity": {
                    "location": image_url
                }
            }
        ],
        "title": "Your image title goes here.",
        "shareMediaCategory": "IMAGE"
    },
    "visibility":{
        "com.linkedin.ugc.MemberNetworkVisibility": "CONNECTION"
    }
}


# share_data = {
#          "author": "urn:li:person:yVc_muusPt",
#          "lifecycleState": "PUBLISHED",
#          "specificContent": {
#          "com.linkedin.ugc.ShareContent": {
#             "shareCommentary": {
#                 "text":"connectify India"
#             },
#             "shareMediaCategory": "IMAGE",
#             "media": [
#                 {
#                     "status": "READY",
#                     "description": {
#                         "text":"Connectify India" 
#                     },
#                     "originalUrl": image_url,
#                     "title": {
#                         "text": "create linkdln profile"
#                     }
#                 }
#             ]
#            }
#           },
#           "visibility": {
#           "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
#           }
#           }

# Set the headers including the access token
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

# Make the POST request to share the image
response = requests.post(share_endpoint, json=share_payload, headers=headers)

# Check the response
if response.status_code == 201:
    print("Image shared successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")
