import requests

# API endpoint for sending messages
api_url = "https://graph.facebook.com/v17.0/109187762280261/messages"

# Your authentication token from WhatsApp
auth_token = "EAALXou3XmgMBO75jNEqlAnLv9GRZCyAZB8Cvy3IjnG00jJhTw7Sc1GywnPEGujpEC3kUvYuhI8wUMZBESDCle03ZA74JAFPTkEMernqZBRwSp7ykqH2hd6TChSdcZAilvSj9FnbxtXGt5nqiWaKtddfdnKp9OQ6L6QMKUuQlLlZB4tsZARnU5QBAMVh0WYz6jcJG4mBibuVHYujvqmvCPen4NmVYcpz2QkLSSkoZD"

# Recipient's phone number (including country code)
recipient_number = "919535943755"

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
