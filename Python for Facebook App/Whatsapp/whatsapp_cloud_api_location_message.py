import requests

# API endpoint for sending messages
api_url = "https://graph.facebook.com/v17.0/109187762280261/messages"

# Your authentication token from WhatsApp
auth_token = "EAAEafQqhaTgBO4wH8BKrYHSml0rVQLneyn1rsD9tjt88Sr9f3dNMKlqbthXkHzIOJ40IrDZCAruuZCkMhkKp7YtEjZBQtGWcL7cZCkVbmHe4t6j6BHpDIKWz58Fxo4T8K0VPBiCooLczwVwwuGZC5ZAbvb5OaNv93iapdfegADhslMLA7I4KQmAwTs7Q3ZBKIr3h7eFVyZB3oK0cYZAbWSmAfgB8DTKWcW062Tboa"

# Recipient's phone number (including country code)
recipient_number = "+917519526081"
image_url='https://cdn.pixabay.com/photo/2015/01/08/18/24/children-593313_1280.jpg'


# Message content
# message_text = "Congratulation!!!!"


# Construct the payload
payload ={
    "messaging_product": "whatsapp",
    "recipient_type":"individual",
    "to": recipient_number,
    "type": "contacts",
    "contacts": [{
      "addresses": [{
          "street": "Sakchi",
          "city": "Jamshedpur",
          "state": "Jharkhand",
          "zip": "831001",
          "country": "India",
          "country_code": "+91",
          "type": "HOME"
        },
        {
          "street": "Harmu",
          "city": "Ranchi",
          "state": "Jharkhand",
          "zip": "834001",
          "country": "India",
          "country_code": "+91",
          "type": "WORK"
        }],
      "birthday": "1990-12-19",
      "emails": [{
          "email": "connectifyindia@hotmail.com",
          "type": "WORK"
        },
        {
          "email": "support123@gmail.com",
          "type": "HOME"
        }],
      "name": {
        "formatted_name": "Kamal Sharma",
        "first_name": "Kamal",
        "last_name": "Sharma",
        "middle_name": "Babu",
        "suffix": "sir",
        "prefix": "CEO"
      },
      "org": {
        "company": "CoonectifyIndia",
        "department": "Legal and NGO",
        "title": "Connecting Global with 1000 of advocate"
      },
      "phones": [{
          "phone": "9535943755",
          "type": "HOME"
        },
        {
          "phone": "9538618870",
          "type": "WORK",
          "wa_id": "9523032118"
        }],
      "urls": [{
          "url": "www.connectifyindia.com",
          "type": "WORK"
        },
        {
          "url": "www.connectifyindia.com/legal",
          "type": "HOME"
        }]
    }]
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
