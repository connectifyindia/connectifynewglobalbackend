import requests

# Your LinkedIn API access token
ACCESS_TOKEN = 'AQXcA5GDthFlDWPrpL_AD4yelLwPKjNEsJGW6Gq-iYexSk8ROgJdpAT9kGDIcyJ1Cbki-2Ow7rWhd4ILOjmU8geRDyxyqpE4HOVWvfjp3woHiAwPEs1Bd73SWrmM7CfTlCbuHEzSf01sSzJKairMBwu1UlhOnQScMqNFiCbNYXHG5bEqx5OVbuBwTw8ENfY87pQxY-GiEvPFV5uTw4ovwP_lxk_n3PeHsqTlGNx8epg5mZT03hm3m_qZPYEG_Dr1sZaGwfsAbDdixcOtQBGzbHNLCfNKEczLoCXgsiCUhhHv1w13xheNjpDPuZgEFwcPQLaLWyVeI5odqi9IEOxf7grZnU7eZw'

# Define the URL for LinkedIn API endpoint
api_url = 'https://api.linkedin.com/v2/shares'

# Define the post content with an image URL
post_data = {
    "content": {
        "contentEntities": [
            {
                "thumbnails": [{"resolvedUrl": "https://connectifyindiasqldb.azurewebsites.net/media/7_Career_Counsel_blog.png"}],
                "resolvedUrl": "https://connectifyindiasqldb.azurewebsites.net/media/7_Career_Counsel_blog.png"
            }
        ],
        "title": "My Image Post",
        "description": "This is a publicly accessible image.",
    },
    "distribution": {
        "linkedInDistributionTarget": {},
    },
    "owner": "urn:li:person:yVc_muusPt",
}

# Define headers with your access token
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
}

# Send the POST request to LinkedIn API
response = requests.post(api_url, json=post_data, headers=headers)

if response.status_code == 201:
    print("Image posted successfully on LinkedIn!")
else:
    print(f"Error posting the image: {response.status_code} - {response.text}")
