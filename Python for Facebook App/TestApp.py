# POST Content As a text
# import requests
# # import facebook
# #Your Access Keys
# page_id_1 = 106234072564818
# # Your Page Access Token
# facebook_access_token_1 = 'EAADlQQRKObIBOyq5KIEKr3MljhFrsVqKbZAoaW53YJ3FKINYDHsS04hsvlsI7JSVgavJwYl7q5ixIaXy1Xg4W8MX2CZCrvoDYPFa1XpdooHLdi9C6YK5nYMHn5FdXZCXtFzWKuodPzsr6iHafbSpo6vM2zbL9QgTZBx0bbgf20lfEdonlqvZCAmo1ibbZAQSCNjcMsvKFkekGZC1CY0LmTrenhp'
# # Post Content as Text
# msg = 'Features are authorization mechanisms that allow apps to access specific types of data through our various APIs. In this way they are similar to Permissions, however Features cannot be granted to an app by an app user. Instead, Features are active or inactive depending on the app user relationship to the app and the app mode when it is being used.'
# post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
# payload = {
# 'message': msg,
# 'access_token': facebook_access_token_1
# }
# r = requests.post(post_url, data=payload)
# print(r.text)

# ***********************************************************************************************#

# POST a Photo
# import requests
# page_id_1 = 106234072564818
# facebook_access_token_1 = "EAADlQQRKObIBOyq5KIEKr3MljhFrsVqKbZAoaW53YJ3FKINYDHsS04hsvlsI7JSVgavJwYl7q5ixIaXy1Xg4W8MX2CZCrvoDYPFa1XpdooHLdi9C6YK5nYMHn5FdXZCXtFzWKuodPzsr6iHafbSpo6vM2zbL9QgTZBx0bbgf20lfEdonlqvZCAmo1ibbZAQSCNjcMsvKFkekGZC1CY0LmTrenhp"
# image_url = 'https://graph.facebook.com/{}/photos'.format(page_id_1)
# msg = 'Hello, this is an automated post from Python!'
# image_location = 'http://connectifyindiasqldb.azurewebsites.net/career_counselling.jpeg'
# img_payload = {
# 'url': image_location,
# 'message': msg,
# 'access_token': facebook_access_token_1
# }
# #Send the POST request
# r = requests.post(image_url, data=img_payload)
# print(r.text)

# *********************************************************************************************#

# Post A video
# import requests
# def upload_video_to_facebook(access_token, video_path, page_id=None):
#     base_url = 'https://graph.facebook.com/'
#     if page_id:
#         upload_url = f'{base_url}{page_id}/videos'
#     else:
#         upload_url = f'{base_url}me/videos'

#     files = {'file': open(video_path, 'rb')}
#     params = {
#         'access_token': access_token,
#     }

#     response = requests.post(upload_url, files=files, params=params)
#     if response.status_code == 200:
#         video_id = response.json()['id']
#         print(f'Video uploaded successfully! Video ID: {video_id}')
#         return video_id
#     else:
#         error_message = response.json().get('error', {}).get('message', 'Unknown error')
#         print(f'Failed to upload video: {error_message}')
#         return None
# # Replace these variables with your actual values
# user_access_token = 'EAAROZCW001VkBO1ZCIT42nZAdohdSia0LGJTyCxSyeI8F66yP1LSsWDndzMlvZCHaIAPAbO2ArqvJKLsZBgURY3gQxLiEuujAj42VSuLZBPM86nN8FZAYfAiYXm9bWCE3TgThtIfLMc686h8SZBR4fELPxtjPiQAlgujxgavnbE5gwxHKpGGBygtT4gcCoZAVbS8ChiDzcRuLpz1ZBAnRJMFxd16qXyGg75IPXqlfrOgkZD'
# page_access_token = 'EAAROZCW001VkBO1ZCIT42nZAdohdSia0LGJTyCxSyeI8F66yP1LSsWDndzMlvZCHaIAPAbO2ArqvJKLsZBgURY3gQxLiEuujAj42VSuLZBPM86nN8FZAYfAiYXm9bWCE3TgThtIfLMc686h8SZBR4fELPxtjPiQAlgujxgavnbE5gwxHKpGGBygtT4gcCoZAVbS8ChiDzcRuLpz1ZBAnRJMFxd16qXyGg75IPXqlfrOgkZD'
# video_file_path = 'd:\Global Project\connectifyindia\public\media\Aspire Legal Access Initiative - A2J Challenge.mp4'
# page_id = 106234072564818  # Optional, set this if you want to upload to a Facebook Page
# # Upload to user's profile
# upload_video_to_facebook(user_access_token, video_file_path)

# **************************************************************************************************#

# POST Video
# import requests
# def publish_video_to_page(page_access_token, page_id, video_path, video_title, video_description):
#     base_url = 'https://graph.facebook.com/'
#     upload_url = f'{base_url}{page_id}/videos'
#     files = {'file': open(video_path, 'rb')}
#     data = {
#         'title': video_title,
#         'description': video_description,
#         'access_token': page_access_token
#     }
#     response = requests.post(upload_url, files=files, data=data)
#     if response.status_code == 200:
#         video_id = response.json()['id']
#         print(f'Video published successfully! Video ID: {video_id}')
#         return video_id
#     else:
#         error_message = response.json().get('error', {}).get('message', 'Unknown error')
#         print(f'Failed to publish video: {error_message}')
#         return None

# # Replace these variables with your actual values
# page_access_token ='EAADlQQRKObIBOyq5KIEKr3MljhFrsVqKbZAoaW53YJ3FKINYDHsS04hsvlsI7JSVgavJwYl7q5ixIaXy1Xg4W8MX2CZCrvoDYPFa1XpdooHLdi9C6YK5nYMHn5FdXZCXtFzWKuodPzsr6iHafbSpo6vM2zbL9QgTZBx0bbgf20lfEdonlqvZCAmo1ibbZAQSCNjcMsvKFkekGZC1CY0LmTrenhp'
# page_id = 106234072564818
# video_file_path = 'd:\Global Project\connectifyindia\public\media\Aspire Legal Access Initiative - A2J Challenge.mp4'
# video_title = 'Legal Aspire'
# video_description = 'Welcome to Connectify India, where we bring together various services under one roof to cater to your career, legal, social, and business needs. Here s a summary of our key features:Career Counseling: We offer top-notch career counseling services for students and professionals. Our platform connects you with experienced counselors who provide personalized guidance, helping you make informed decisions about your educational and professional journey.Legal Services: Connectify India provides legal services to consumers in need. Our team of expert advocates offers legal advice, assistance, and representation in various areas, ensuring access to justice and protection of your rights.Social Services: We connect NGOs and social service organizations to create a positive impact on society. By bridging the gap between those in need and those willing to help, we facilitate collaborations and enable collective efforts towards social welfare.Business Connection: Our platform connects businesses with consumers, ensuring informed decision-making. Whether you are looking for products, services, or business partnerships, Connectify India provides a platform for seamless interactions and networking opportunities.As we continue to expand our reach, our vision extends beyond India to target the global market. Join us today and let Connectify India empower you to make the best choices for your future.'
# # Publish the video to the Facebook Page
# publish_video_to_page(page_access_token, page_id, video_file_path, video_title, video_description)

# ***********************************************************************************************************#

# Multple Post
# import requests

# def create_carousel_post(page_access_token, page_id, carousel_items):
#     base_url = 'https://graph.facebook.com/'
#     publish_url = f'{base_url}{page_id}/feed'

#     carousel_payload = {
#         'access_token': page_access_token,
#         'child_attachments': carousel_items
#     }

#     response = requests.post(publish_url, json=carousel_payload)

#     if response.status_code == 200:
#         post_id = response.json()['id']
#         print(f'Carousel post created successfully! Post ID: {post_id}')
#         return post_id
#     else:
#         error_message = response.json().get('error', {}).get('message', 'Unknown error')
#         print(f'Failed to create carousel post: {error_message}')
#         return None

# # Replace these variables with your actual values
# page_access_token = 'EAAROZCW001VkBO1ZCIT42nZAdohdSia0LGJTyCxSyeI8F66yP1LSsWDndzMlvZCHaIAPAbO2ArqvJKLsZBgURY3gQxLiEuujAj42VSuLZBPM86nN8FZAYfAiYXm9bWCE3TgThtIfLMc686h8SZBR4fELPxtjPiQAlgujxgavnbE5gwxHKpGGBygtT4gcCoZAVbS8ChiDzcRuLpz1ZBAnRJMFxd16qXyGg75IPXqlfrOgkZD'
# page_id = 109989205132383

# # List of carousel items (multiple images and content)
# carousel_items = [
#     {
#         'name': 'Simply Counsel',
#         'link': 'https://www.connectifyindia.com/',
#         'picture': 'http://connectifyindiasqldb.azurewebsites.net/6_Career_Counsel_Blog_4u2IrOf.png',
#         'description': 'It is important to note that copyright laws can be complex and can vary from one country to another. Therefore, individuals and businesses should consult with legal professionals who specialize in copyright law to understand their rights and potential legal consequences in their specific jurisdiction.'
#     },
#     {
#         'name': 'Business Connect',
#         'link': 'https://dirums.com/',
#         'picture': 'http://connectifyindiasqldb.azurewebsites.net/5_Project_Connect_Homepage.png',
#         'description': 'The answer to this question depends on the employment laws and regulations of the specific jurisdiction in which the employer operates. In many countries, including the United States, the default employment relationship is known as at-will employment.Under this arrangement, an employer generally has the right to terminate an employee without providing a reason, as long as the termination does not violate any specific laws or employment contracts. However, there are exceptions to this rule. For example, anti-discrimination laws prohibit employers from terminating employees based on factors such as race, gender, religion, disability, or age. Additionally, certain employment contracts may contain provisions that limit the employer'
#     },
#     # Add more carousel items as needed
# ]
# # Create the carousel post on the Facebook Page
# create_carousel_post(page_access_token, page_id, carousel_items)

# import requests
# def post_multiple_images_with_link(page_access_token, page_id, image_urls, link_url, link_caption, link_description):
#     base_url = 'https://graph.facebook.com/'

#     # Create a list of tuples containing image URLs and names
#     images = [(f'image{i + 1}', open(image_url, 'rb')) for i, image_url in enumerate(image_urls)]

#     # Add the link parameters
#     params = {
#         'access_token': page_access_token,
#         'url': link_url,
#         'caption': link_caption,
#         'description': link_description
#     }

#     # Combine the images and link parameters in the request
#     response = requests.post(f'{base_url}{page_id}/photos', files=images, data=params)

#     if response.status_code == 200:
#         post_id = response.json()['post_id']
#         print(f'Multiple images with link posted successfully! Post ID: {post_id}')
#         return post_id
#     else:
#         error_message = response.json().get('error', {}).get('message', 'Unknown error')
#         print(f'Failed to post multiple images with link: {error_message}')
#         return None

# # Replace these variables with your actual values
# page_access_token = 'EAAChCJiYdz0BO9CrT4MP5HSCgh9FMBK3aDh1P2VW6tteGgiOk9D8kcaeoyaGuR3KWD6EOvDijD0Ga0C6ZB92ZAoZByVdymm7uP2q2iehhAT3jv5Vjb8iBiZBcNZC3vZB8ZBZAuVZAl61lnuAUBT5xngC2rRRR17j59njHWKSQDCJhrTbGtW4w1vZAuNmQ2BKnZBkl11J8YXTJGCDs4d4ZAFZC2JavngnWHtquDHZCSEPyWitwZD'
# page_id = 102046439274468
# image_urls = ['http://connectifyindiasqldb.azurewebsites.net/career_counselling.jpeg']
# link_url = 'https://www.connectifyindia.com/'
# link_caption = 'Check out this website!'
# link_description = 'This website has some interesting content.'

# # Post multiple images with the link to the Facebook Page
# post_multiple_images_with_link(page_access_token, page_id, image_urls, link_url, link_caption, link_description)




# import requests

# def post_link_on_facebook(user_access_token, link_url, link_caption, link_description):
#     base_url = 'https://graph.facebook.com/'
#     post_url = f'{base_url}102046439274468/feed'

#     link_payload = {
#         'access_token': user_access_token,
#         'link': link_url,
#         'caption': link_caption,
#         'description': link_description
#     }

#     response = requests.post(post_url, data=link_payload)

#     if response.status_code == 200:
#         post_id = response.json()['id']
#         print(f'Link posted successfully! Post ID: {post_id}')
#         return post_id
#     else:
#         error_message = response.json().get('error', {}).get('message', 'Unknown error')
#         print(f'Failed to post link: {error_message}')
#         return None

# # Replace these variables with your actual values
# user_access_token = 'EAAChCJiYdz0BO9CrT4MP5HSCgh9FMBK3aDh1P2VW6tteGgiOk9D8kcaeoyaGuR3KWD6EOvDijD0Ga0C6ZB92ZAoZByVdymm7uP2q2iehhAT3jv5Vjb8iBiZBcNZC3vZB8ZBZAuVZAl61lnuAUBT5xngC2rRRR17j59njHWKSQDCJhrTbGtW4w1vZAuNmQ2BKnZBkl11J8YXTJGCDs4d4ZAFZC2JavngnWHtquDHZCSEPyWitwZD'
# link_url = 'https://www.connectifyindia.com/'
# link_caption = 'Check out this website!'
# link_description = 'This website has some interesting content.'

# # Post the link on the authenticated user's timeline
# post_link_on_facebook(user_access_token, link_url, link_caption, link_description)



# import requests

# def post_multiple_images_as_carousel(page_access_token, page_id, image_urls):
#     base_url = 'https://graph.facebook.com/'
#     post_url = f'{base_url}{page_id}/photos'

#     # Create a list of tuples containing image URLs and names
#     images = [(f'image{i,i+1}', open(image_url,'rb')) for i, image_url in enumerate(image_urls)]
#     print(images)
#     carousel_payload = {
#         'access_token': page_access_token,
#         'published': 'true',  # Set to 'true' if you want to publish immediately
#     }

#     # Combine the images in the carousel
#     response = requests.post(post_url, data=carousel_payload, files=images)

#     if response.status_code == 200:
#         post_id = response.json()['id']
#         print(post_id)
#         print(f'Carousel post created successfully! Post ID: {post_id}')
#         # return post_id
#     else:
#         error_message = response.json().get('error', {}).get('message', 'Unknown error')
#         print(f'Failed to create carousel post: {error_message}')
#         return None

# # Replace these variables with your actual values
# page_access_token = 'EAANabfG6BOgBOZCZCILjjQfJIXIsXIAnWmIHZBNKz1oUFxtlyWGMZBZALeOhmkwBeoVOycaXcDoEIwjoXMlpBy6wukKzZAGrkOA4ZCyAdqx61UjJhpYTs9tVQ2gq77m2kiiLn4gejNgvjZBennyPQIMnxrjDNtCozR47tJAlyCsDAcxDgubG9xo4nsa9NJIwGAsK0ZAGQz9M0USZBkZBTnh1V21olABNW8ZAlxJpxHqGY9daZAwZDZD'
# page_id = 2208240272776646
# image_urls = ['d:\Global Project\connectifyindia\public\images\AINAW.png','d:\Global Project\connectifyindia\public\images\ALMAU.png']
# # Post the images as a carousel on the Facebook Page
# post_multiple_images_as_carousel(page_access_token, page_id, image_urls)

# ***********************************************************************************************************#



# def get_page_access_token(user_access_token, page_id):
#     # Get the Page Access Token from the User Access Token
#     url = f"https://graph.facebook.com/{page_id}"
#     params = {
#         "fields": "access_token",
#         "access_token": user_access_token
#     }

#     response = requests.get(url, params=params)
#     data = response.json()
#     page_access_token = data.get("access_token")
#     return page_access_token

# def post_to_facebook_page(page_id, page_access_token, message, privacy="EVERYONE"):
#     # Post the message to the Facebook Page with the specified privacy setting
#     url = f"https://graph.facebook.com/{page_id}"
#     params = {
#         "access_token": page_access_token,
#         "message": message,
#         "privacy": {"value": privacy}
#     }

#     response = requests.post(url, params=params)
#     return response.json()

# if __name__ == "__main__":
#     # Replace these values with your own credentials
#     user_access_token = "EAAROZCW001VkBO9OJnZAdnLUCz5a9GyZAl6WZBOhnTsbDQeumsvEFSebuJIjZCd9t4Gsxw8cndsEvvyA0s2kyd6W0iKHnbTMGXivZBTzpzRs30L4PnPDQRKJJyVm8CakiaHnsC8KNl2GZCw8WBj7xw0zlEQKegEY6EEqTWdnuaRbutCqDww0yWltcg5MyvhjOENHiYExkBjIMiKlvAVb2nl8e9rNiccgZBrsYH0d5DAZD"
#     page_id = 109989205132383
#     message_to_post = "Hello, this is a test post with specific privacy settings!"

#     page_access_token = get_page_access_token(user_access_token, page_id)
#     if page_access_token:
#         response_data = post_to_facebook_page(page_id, page_access_token, message_to_post)
#         print("Post successful! Post ID:", response_data.get("id"))
#     else:
#         print("Failed to obtain Page Access Token.")





# import requests
# def post_multiple_photos(page_id, access_token, photo_urls, message=None):
#     api_version = "v17.0"  # Update to the latest Graph API version
#     endpoint = f"https://graph.facebook.com/{api_version}/{page_id}/photos"

#     # Prepare the payload
#     payload = {
#         "access_token": access_token,
#         "url": photo_urls,
#         "published": "false"  # To create an unpublished post
#     }

#     if message:
#         payload["caption"] = message

#     try:
#         response = requests.post(endpoint, data=payload)
#         response.raise_for_status()
#         print("Photos posted successfully!")
#     except requests.exceptions.RequestException as e:
#         print(f"Error posting photos: {e}")

# if __name__ == "__main__":
#     # Replace these variables with your own values
#     page_id = 2208240272776646
#     access_token = "EAANabfG6BOgBOZCZCILjjQfJIXIsXIAnWmIHZBNKz1oUFxtlyWGMZBZALeOhmkwBeoVOycaXcDoEIwjoXMlpBy6wukKzZAGrkOA4ZCyAdqx61UjJhpYTs9tVQ2gq77m2kiiLn4gejNgvjZBennyPQIMnxrjDNtCozR47tJAlyCsDAcxDgubG9xo4nsa9NJIwGAsK0ZAGQz9M0USZBkZBTnh1V21olABNW8ZAlxJpxHqGY9daZAwZDZD"
#     photo_urls = [
#         "http://connectifyindiasqldb.azurewebsites.net/career_counselling.jpeg",
#         "http://connectifyindiasqldb.azurewebsites.net/Business_services.png",
#         "http://connectifyindiasqldb.azurewebsites.net/Connecting_Legal.png",
#         # Add more photo URLs if needed
#     ]
#     message = "Optional message for the post"

#     post_multiple_photos(page_id, access_token, photo_urls, message)





# import facebook

# def upload_photo_with_resumable_upload(access_token, photo_urls):
#     try:
#         graph = facebook.GraphAPI(access_token)

#         # Upload each photo
#         for photo_url in photo_urls:
#             # Start the resumable upload session for the photo
#             resumable_url = graph.put_object(
#                 parent_object="me",
#                 connection_name="photos",
#                 file_url=photo_url,
#                 chunked=True,
#                 resumable=True
#             )

#             # Upload the photo in chunks
#             with open(photo_url, "rb") as photo_file:
#                 chunk_size = 4 * 1024 * 1024  # 4 MB chunks
#                 while True:
#                     chunk = photo_file.read(chunk_size)
#                     if not chunk:
#                         break

#                     graph.put_object(
#                         parent_object=resumable_url,
#                         connection_name="",
#                         chunked=True,
#                         resumable=True,
#                         data=chunk
#                     )

#             print(f"Photo uploaded successfully: {photo_url}")
#     except facebook.GraphAPIError as e:
#         print(f"Error uploading photo: {e}")


# if __name__ == "__main__":
#     # Replace this variable with your own access token
#     access_token = "EAANabfG6BOgBO9TExioiU0dCIq6ZADDoPNZBPcZALkltPyCEFJCvMA4yZBfVyZBPTBxHC901jHd7rrXCnZC0zXp7jLQvUPEuxmcxwkl6SUJHcAnKEHEzZCN1z3QZAiMv4yS4aiNdPMR5ZADuuxBALomibAYf6PtRHks33KfxkZC8ZAZBXw24m2oaeSNLfdJ27hMxoHiLv6RujvZAslL1qpaIfDGpILLiwtYtyFw4FYZBb1lmSL"

#     # Replace this list with the paths to the photos you want to upload
#     photo_urls = [
#         "http://connectifyindiasqldb.azurewebsites.net/career_counselling.jpeg",
#         "http://connectifyindiasqldb.azurewebsites.net/Business_services.png",
#         "http://connectifyindiasqldb.azurewebsites.net/Connecting_Legal.png",
#         # Add more photo URLs if needed
#     ]

#     upload_photo_with_resumable_upload(access_token, photo_urls)







# import requests

# def create_album_with_resumable_upload(access_token, album_name, photo_urls, message=None):
#     try:
#         # Create the album
#         url = f"https://graph.facebook.com/me/albums"
#         params = {
#             "access_token": access_token,
#             "name": album_name,
#         }
#         if message:
#             params["message"] = message

#         response = requests.post(url, params=params)
#         response_data = response.json()
#         album_id = response_data.get("id")

#         if not album_id:
#             print("Error creating the album.")
#             return

#         print(f"Album '{album_name}' created with ID: {album_id}")

#         # Upload photos to the album
#         for photo_url in photo_urls:
#             upload_photo_to_album(album_id, access_token, photo_url)

#         print("Photos uploaded successfully!")
#     except requests.RequestException as e:
#         print(f"Error uploading photos: {e}")


# def upload_photo_to_album(album_id, access_token, photo_url):
#     try:
#         # Start the resumable upload session for the photo
#         url = f"https://graph.facebook.com/{album_id}/photos"
#         params = {
#             "access_token": access_token,
#             "url": photo_url,
#         }

#         response = requests.post(url, params=params)
#         response_data = response.json()

#         if "error" in response_data:
#             print(f"Error uploading photo: {response_data['error']['message']}")
#         else:
#             print(f"Photo uploaded successfully: {photo_url}")
#     except requests.RequestException as e:
#         print(f"Error uploading photo: {e}")


# if __name__ == "__main__":
#     # Replace this variable with your own access token
#     access_token = "EAANabfG6BOgBO9TExioiU0dCIq6ZADDoPNZBPcZALkltPyCEFJCvMA4yZBfVyZBPTBxHC901jHd7rrXCnZC0zXp7jLQvUPEuxmcxwkl6SUJHcAnKEHEzZCN1z3QZAiMv4yS4aiNdPMR5ZADuuxBALomibAYf6PtRHks33KfxkZC8ZAZBXw24m2oaeSNLfdJ27hMxoHiLv6RujvZAslL1qpaIfDGpILLiwtYtyFw4FYZBb1lmSL"

#     # Replace this list with the URLs of the photos you want to upload
#     photo_urls = [
#         "http://connectifyindiasqldb.azurewebsites.net/career_counselling.jpeg",
#         "http://connectifyindiasqldb.azurewebsites.net/Business_services.png",
#         "http://connectifyindiasqldb.azurewebsites.net/Connecting_Legal.png",
#         # Add more photo URLs if needed
#     ]

#     album_name = "Connects Global"
#     message = "Optional message for the album"

#     create_album_with_resumable_upload(access_token, album_name, photo_urls, message)

# import requests
# def upload_large_file(access_token, file_path):
#     try:
#         # Open the file and get its size
#         with open(file_path, "rb") as file:
#             file_size = len(file.read())

#             print(int(file_size))

#         # Initialize the upload session
#         params = {
#             "access_token": access_token,
#             "upload_phase": "start",
#             "file_size": file_size,
#         }
#         response = requests.post("https://graph.facebook.com/v17.0/me/videos", params=params)
#         response_data = response.json()

#         if "video_id" not in response_data:
#             print(f"Error starting upload: {response_data['error']['message']}")
#             return

#         # Get the video ID and upload session ID
#         video_id = response_data["video_id"]
#         upload_session_id = response_data["upload_session_id"]

#         # Perform chunked uploads
#         chunk_size =  4*1024 * 1024  # 4 MB chunks
#         offset = 0
#         while int(offset) < file_size:
#             chunk = min(chunk_size, file_size - offset)
#             params = {
#                 "access_token": access_token,
#                 "upload_phase": "transfer",
#                 "start_offset": offset,
#                 "upload_session_id": upload_session_id,
#             }

#             # Read the chunk from the file
#             with open(file_path, "rb") as file:
#                 file.seek(offset)
#                 chunk_data = file.read(chunk)

#             files = {
#                 "video_file_chunk": chunk_data
#             }

#             response = requests.post("https://graph.facebook.com/v12.0/me/videos", params=params, files=files)
#             response_data = response.json()

#             if "start_offset" in response_data:
#                 # Offset was returned, continue from the returned offset
#                 offset = response_data["start_offset"]
#             elif "video_id" in response_data:
#                 # Successfully uploaded the chunk
#                 offset += chunk
#             else:
#                 print(f"Error uploading chunk: {response_data['error']['message']}")
#                 return

#         # Finish the upload
#         params = {
#             "access_token": access_token,
#             "upload_phase": "finish",
#             "upload_session_id": upload_session_id,
#         }
#         response = requests.post("https://graph.facebook.com/v12.0/me/videos", params=params)
#         response_data = response.json()
#         print(response_data)

#         if "video_id" not in response_data:
#             print(f"Error finishing upload: {response_data['error']['message']}")
#             return

#         print("Upload completed successfully!")
#     except requests.RequestException as e:
#         print(f"Error during upload: {e}")


# if __name__ == "__main__":
#     # Replace this variable with your own access token
#     access_token = "EAANabfG6BOgBO9TExioiU0dCIq6ZADDoPNZBPcZALkltPyCEFJCvMA4yZBfVyZBPTBxHC901jHd7rrXCnZC0zXp7jLQvUPEuxmcxwkl6SUJHcAnKEHEzZCN1z3QZAiMv4yS4aiNdPMR5ZADuuxBALomibAYf6PtRHks33KfxkZC8ZAZBXw24m2oaeSNLfdJ27hMxoHiLv6RujvZAslL1qpaIfDGpILLiwtYtyFw4FYZBb1lmSL"

#     # Replace this variable with the path to the large file you want to upload
#     file_path = "d:\Global Project\connectifyindia\public\media\short_video.mp4"

#     upload_large_file(access_token, file_path)

# Sample list of dictionaries
# data = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25},
#     {"name": "Charlie", "age": 35}
# ]

# # Iterate over the list of dictionaries
# for item in data:
#     # Access each dictionary
#     print("Name:", item["name"])
#     print("Age:", item["age"])
#     print("----")

