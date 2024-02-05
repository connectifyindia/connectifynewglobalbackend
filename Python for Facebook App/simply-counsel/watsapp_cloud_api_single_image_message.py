import requests

# API endpoint for sending messages
api_url = "https://graph.facebook.com/v17.0/109187762280261/messages"

# Your authentication token from WhatsApp
auth_token = "EAALXou3XmgMBOZB1zPNuDgSfHyq892o6PqFS9S6qe0K6DaK2DUxBOComMkZA5cVtuRM2zT6MCK9eSKgjWRcdlgOar2tnLK6GkUKkjgvT1UZBssszbH2krfHY3TZBdGGKKJWOGZBwBJfriqo53YvURhGrx1l1rxAUsxDr0yDnX2A4h77LZAkZCHv33PuUZAynMZAExJL6cFRCYT6PrZByFP4FWPkn8TfJcuOtDYSnwZD"

# Recipient's phone number (including country code)
recipient_number = "917519526081"
image_url='https://d2wmjgcwxowcvo.cloudfront.net/download-2022.1.23_19.7.26-dirums-(dirums.com)/media/raksha-bandhan-offer-banner-dirums%20(1).jpg'


# Message content
# message_text = "Congratulation!!!!"


# Construct the payload
payload ={
    "messaging_product": "whatsapp",
    "recipient_type":"individual",
    "to": recipient_number,
    "type":"image",
    "image":{
        "link":image_url
        }
  }

# Headers with authentication token
headers = {
    "Authorization": f"Bearer {auth_token}",
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(api_url, json=payload, headers=headers)

if response.status_code == 200:
    print("Message sent successfully!")
    print(response.text)
else:
    print("Failed to send message:", response.text)
