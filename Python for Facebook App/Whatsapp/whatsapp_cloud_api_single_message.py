import requests

# API endpoint for sending messages
api_url = "https://graph.facebook.com/v17.0/109187762280261/messages"

# Your authentication token from WhatsApp
auth_token = "EAAEafQqhaTgBO4wH8BKrYHSml0rVQLneyn1rsD9tjt88Sr9f3dNMKlqbthXkHzIOJ40IrDZCAruuZCkMhkKp7YtEjZBQtGWcL7cZCkVbmHe4t6j6BHpDIKWz58Fxo4T8K0VPBiCooLczwVwwuGZC5ZAbvb5OaNv93iapdfegADhslMLA7I4KQmAwTs7Q3ZBKIr3h7eFVyZB3oK0cYZAbWSmAfgB8DTKWcW062Tboa"

# Recipient's phone number (including country code)
recipient_number = "917519526081"

# Message content
message_text = "Congratulation!!!!"

# Construct the payload
payload = {
    "recipient_type": "individual",
    "to": recipient_number,
    "type": "text",
    "text": {
        "body": message_text
    },
    "messaging_product": "whatsapp",
    # "template": {
    #      "name": "hello_world", "language": { "code": "en_US" }
    #        }
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
else:
    print("Failed to send message:", response.text)
