import requests

page_id_1=input("Enter Page ID 1 =")
page_access_tokens1=input("Enter Page Access Token 1 =")
# *************************************************************

page_id_2=input("Enter Page ID 2 =")
page_access_tokens2=input("Enter Page Access Token 2 =")
# *************************************************************

page_id_3=input("Enter Page ID 3 =")
page_access_tokens3=input("Enter Page Access Token 3 =")
# *************************************************************

page_id_4=input("Enter Page ID 4 =")
page_access_tokens4=input("Enter Page Access Token 4 =")
# *************************************************************

page_id_5=input("Enter Page ID 5 =")
page_access_tokens5=input("Enter Page Access Token 5 =")
# *************************************************************

page_id_6=input("Enter Page ID 6 =")
page_access_tokens6=input("Enter Page Access Token 6 =")
# *************************************************************

page_access_tokens = {
    page_id_1:page_access_tokens1,
    page_id_2:page_access_tokens2,
    page_id_3:page_access_tokens3,
    page_id_4:page_access_tokens4,
    page_id_5:page_access_tokens5,
    page_id_6:page_access_tokens6
    # Add more page IDs and access tokens as needed
}

# page_access_tokens = {
#     '102046439274468':'EAAEafQqhaTgBOZCiWSsZAZAZAi6nfiqxlibxIfCBmZA3vZBzRKeftJKwhfE8pBPVF4diR8b3DFwPpKL3EZCZA0nZBxTQMtaFZCP8DAmkwc0uz5s4x35TcI4trdFe0lRIZBqDZC4hOGkvQxZAZAlYGj0aVy7MSJPwwiRRNd40mU5NZBU0UyIe4CUC8aZCWSLqjujToooC8NgYx9ZCUQGLiBEYZAdjFN2EEMatlBvw7HdAqDaf8RTon2',
#     '108767425426932':'EAAEafQqhaTgBO9GiilzUewGcOdAVZAFa9iJdYE3DPJNOsEiyeUrDTuWAzUvW8zxzO4e7hA3DnAQfZBNL3HUyYkti107I53re3JSZBO0NQFLOZB76itQbFEZATyBQVMzzgVid2L6SCAagE9nPOA6T4fMBQPPfToGDrsU2jZCQAqO5ZBzlaPK8oNJ2f7WeLvzhk85Yztaqhz2bpZCof8NfNyrfSybR0Of9wya7qr0d0MQZD',
#     '109989205132383':'EAAEafQqhaTgBO0aZA4GT7ZC2FVIQPXZBCO6zZBPtWTqJL8tIpMwitPzBeL9aOSf031h97xARZBBTX71oWtNZA86VZA2ASNXJfwHOZAwU6pHWx7iZC6OPkeYsixergx5GiQLzCQKyzLbE7d8g4gQrkjtOjJkDofqYAm5wvYU3MXru8bft3lZCtlEU3nG1lDUvw4mugw71ZCuZCZAwpX6zoc2zTEB7prVXUSPuhZCm285kYqra3T',
#     '102284272129785':'EAAEafQqhaTgBOyv4gK76FIWSLcZBrfuXnAAFG2xT7GF8B6gknSTmddzDZAZB17l5ITaZB2jCnu1Tw9ZAs4SgqJnuyMAfmBnVTcP9bc2DIvObDvaS2wvrHKlgjGv2PTjD1avJU4i1kG0VjGr5KFMN0ZBuViByoBZA14KLctvc0rvyRhV3lTCu5uRT667i2tcrmFfhrn1DWVf4eM21VoSpMks7OZAptNkVIetS9GtZBQv4P'
#     # Add more page IDs and access tokens as needed
# }
message = """Description
Tiranga; Tricolour, Proportion 2:3, Flag of India."""
image_url="https://media.istockphoto.com/id/472317739/vector/flag-of-india.jpg?s=612x612&w=0&k=20&c=ejlQRX4C_Mb40wz1JQcB5vKYcOKlfRtry2W6UcX6mlo="
# file_url="d:\Global Project\connectifyindia\public\media\short_video.mp4"
for page_id, access_token in page_access_tokens.items():
    payload = {
        'message': message,
        # 'description': message,
        'access_token': access_token,
        'url':image_url
        # 'files':file_url
        }
    response = requests.post(f'https://graph.facebook.com/v17.0/{page_id}/photos', data=payload)
    # response = requests.post(f'https://graph.facebook.com/v17.0/{page_id}/videos', data=payload)
    if response.status_code == 200:
        print(f"Message posted on page {page_id}")
    else:
        print(f"Failed to post on page {page_id}: {response.text}")