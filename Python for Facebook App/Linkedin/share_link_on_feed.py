import requests
# Replace with your LinkedIn API credentials
client_id = '77slg2z6ytu5oj'
client_secret = 'HwL4fXqgtatBAvDw'
access_token = 'AQX6U1u7agaLAPj3-MDfIk8YGlZpSJP1cH3DsgtBYpo1nrVcUxswmUzC-3QqcXBGLfOWM3geThEC8qKKZYpLl_52Tusq36wFq1KoL8ve_Gyfq-EGN3_v8A2ddc1ZegPoT2MBNM1zx9tcvTV5zCY-sQozP3SO7ZjKXe1cOBbxXLlFp2Zc2io5RebdblbGMXsdmZxaLv2TPe3Xj-lxUe8GzE2jAL1zxk1sKAXfc3BtIAZjnAIxl5Ue4pAwuRsE-T2vmp0Y7tX53r4fI3mTJB_BKRXBcj4Ug4RMh_s79M6XvU7amES4j2SuInAQs6AuUesBjXhD4cBaMsu49ofcHLSP-BEtbVVVhQ'

# Define the URL you want to share
share_url = 'https://youtu.be/8tEVEi4Zq38?si=5LU2KaZ26nniT-Pk'

# Set the request headers
headers = {
    'X-Restli-Protocol-Version': '2.0.0',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}',
}

# Create the JSON payload for sharing the URL
payload = {
    'content': {
        'contentEntities': [
            {
                'entityLocation': share_url,
            }
        ],
        'title': 'Check out this link!',
    },
    'visibility': {
        'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC',
    },
}

# Send a POST request to share the URL
response = requests.post('https://api.linkedin.com/v2/ugcPosts', headers=headers, json=payload)

# Check the response
if response.status_code == 201:
    print('URL shared successfully on LinkedIn.')
else:
    print(f'Error sharing URL: {response.status_code} - {response.text}')



# curl --upload-file /Users/peter/Desktop/superneatimage.png --header "Authorization: Bearer redacted" 'https://api.linkedin.com/mediaUpload/C5522AQGTYER3k3ByHQ/feedshare-uploadedImage/0?ca=vector_feedshare&cn=uploads&m=AQJbrN86Zm265gAAAWemyz2pxPSgONtBiZdchrgG872QltnfYjnMdb2j3A&app=1953784&sync=0&v=beta&ut=2H-IhpbfXrRow1'