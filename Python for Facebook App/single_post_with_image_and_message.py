import requests
page_id_1 = '102046439274468'
facebook_access_token_1 = "EAADdLTy4LjcBOzgXYHbM1P5Yg6SE5h8AjcBfzHD5jahZCth0jOzimcxrWvDko2J6cy7doe2HoQuTz6dxEvC85eDjJWgdyC2JkflGhtoloZCGsq7WrW5rWZAs3ZA8UdqDQcLNLX29ZCrXFsjPgN8ZBmDTnxPSdSG5G44OsRvG5TDwaPjXJk1KGsTikuEa1nCZBN81KAvd9qCck6jfrjOCqYZBL58FHdXaWzDT2WacwHcZD"
image_url = 'https://graph.facebook.com/{}/photos'.format(page_id_1)
msg = 'Our Fellows work in Rural Development across these 12 thematic areas posted on date 8/2/2023 at 7:11 pm IST https://www.connectifyindia.com/ainaw'
image_location= 'https://www.connectifyindia.com/_next/image?url=%2Fimages%2Fgirl.jpg&w=256&q=80'
img_payload = {
'url': image_location,
'message': msg,
'access_token': facebook_access_token_1
}
#Send the POST request
r = requests.post(image_url, data=img_payload)
print(r.text)


