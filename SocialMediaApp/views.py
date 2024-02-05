from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ConnectifyIndia,SimplyCounsel,LegalAspire,Ainaw,BusinessConnect,Instagram,Twiter,Linkedln,Telegram,Whatsapp,FacebookModel
from .serializer import ConnectifyIndiaSerializer,SimplyCounselSerializer,InstagramSerializer,LegalAspireSerializer,AinawSerializer,BusinessConnectSerializer,TwiterSerializer,LinkedlnSerializer,TelegramSerializer,WhatsappSerializer,FacebookSerializer
import time
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import generics
import requests
from django.shortcuts import render
# from django.http import HttpResponse
import os
import facebook
from rest_framework import status
import json
import tweepy

class ConnectifyIndiaListCreateApiView(generics.ListCreateAPIView):
     queryset=ConnectifyIndia.objects.all()
     serializer_class=ConnectifyIndiaSerializer

class ConnectifyIndiaRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
     queryset=ConnectifyIndia.objects.all()
     serializer_class=ConnectifyIndiaSerializer

# ***************************New Model********************************

class FacebookListCreateApiView(generics.ListCreateAPIView):
     queryset=FacebookModel.objects.all()
     serializer_class=FacebookSerializer

class FacebookRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
     queryset=FacebookModel.objects.all()
     serializer_class=FacebookSerializer

# ***********************************************************************

class SimplyCounselListCreateApiView(generics.ListCreateAPIView):
     queryset=SimplyCounsel.objects.all()
     serializer_class=SimplyCounselSerializer
class SimplyCounselRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
     queryset=SimplyCounsel.objects.all()
     serializer_class=SimplyCounselSerializer

class LegalAspireListCreateApiView(generics.ListCreateAPIView):
     queryset=LegalAspire.objects.all()
     serializer_class=LegalAspireSerializer
class LegalAspireRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
     queryset=LegalAspire.objects.all()
     serializer_class=LegalAspireSerializer

class AinawListCreateApiView(generics.ListCreateAPIView):
     queryset=Ainaw.objects.all()
     serializer_class=AinawSerializer
class AinawRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Ainaw.objects.all()
     serializer_class=AinawSerializer

class BusinessConnectListCreateApiView(generics.ListCreateAPIView):
     queryset=BusinessConnect.objects.all()
     serializer_class=BusinessConnectSerializer
class BusinessConnectRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
     queryset=BusinessConnect.objects.all()
     serializer_class=BusinessConnectSerializer

class InstagramListCreateApiView(generics.ListCreateAPIView):
     queryset=Instagram.objects.all()
     serializer_class=InstagramSerializer
class InstagramRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Instagram.objects.all()
     serializer_class=InstagramSerializer

class TwiterListCreateApiView(generics.ListCreateAPIView):
     queryset=Twiter.objects.all()
     serializer_class=TwiterSerializer
class TwiterRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Twiter.objects.all()
     serializer_class=TwiterSerializer

class LinkedlnListCreateApiView(generics.ListCreateAPIView):
     queryset=Linkedln.objects.all()
     serializer_class=LinkedlnSerializer
class LinkedlnRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Linkedln.objects.all()
     serializer_class=LinkedlnSerializer

class TelegramListCreateApiView(generics.ListCreateAPIView):
     queryset=Telegram.objects.all()
     serializer_class=TelegramSerializer
class TelegramRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Telegram.objects.all()
     serializer_class=TelegramSerializer

class WhatsappListCreateApiView(generics.ListCreateAPIView):
     queryset=Whatsapp.objects.all()
     serializer_class=WhatsappSerializer
class WhatsappRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Whatsapp.objects.all()
     serializer_class=WhatsappSerializer

     #*****************************CONNECTIFY INDIA****************************************  
class Text_post_to_connectifyindia_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = ConnectifyIndia.objects.all().values('content','fb_page_id','fb_page_access_token','link_url')  # Fetch necessary fields
        print(posts)
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = f"Content: {post['content']}"
                link_url = post['link_url']
               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i], access_tokens[i], message,link_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message,link_url):
    import requests
    
    url = f"https://graph.facebook.com/{page_id}/feed"
    params = {
        'message': message,
        'access_token': access_token,
        'link':link_url
    }
    
    response = requests.post(url, params=params)
    return response.json()  # Returns the response from the Facebook API


class Image_post_to_connectifyindia_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = ConnectifyIndia.objects.all().values('content','fb_page_id','fb_page_access_token','image_url')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  image_url = post['image_url']
                # http_url=post['image_url']
                # response = requests.head(http_url, allow_redirects=True)
                # image_url = response.url
                image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"


               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i],access_tokens[i],message,image_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message, image_url):
    import requests
    
    upload_url = f"https://graph.facebook.com/v17.0/{page_id}/photos"
    params = {
        'message': message,
        'access_token': access_token,
        'url':image_url,
    }
    
    response = requests.post(upload_url,params=params)
    return response.json()  # Returns the response from the Facebook API

class Video_post_to_connectifyindia_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = ConnectifyIndia.objects.all().values('content','fb_page_id','fb_page_access_token','video_url')  # Fetch necessary fields
        print(posts)
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  image_url = post['image_url']
               #  http_url=post['video_url']
               #  response = requests.head(http_url, allow_redirects=True)
               #  video_url = response.url
                video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_4.mp4"
               #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"


               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i],access_tokens[i],message,video_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message,video_url):
    import requests
    
    video_response = requests.post(f'https://graph-video.facebook.com/{page_id}/videos',
              files={'source': video_url},
                # files={'source': open('d:\Global Project\connectifyindia\public\media\short_video1.mp4', 'rb')},

         params={
            'access_token':access_token,
            'description':message
            }
            )
    if video_response.status_code == 200:
           video_id = video_response.json()['id']
           post_response = requests.post(
            f'https://graph.facebook.com/{page_id}/feed',
           params={
                'description':message,
                'attached_media[0]': f'{{"media_fbid":"{video_id}"}}',
                'access_token': access_token,
            }
           )
    if video_response.status_code == 200:
            print(f"Posted to Facebook Page {page_id} successfully.")
    else:
            print(f"Failed to post on page {page_id}: {video_response.text}")

class Link_post_to_connectifyindia_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = ConnectifyIndia.objects.all().values('content','fb_page_id','fb_page_access_token','link_url')  # Fetch necessary fields
        print(posts)

        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
                link_url = post['link_url']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i], access_tokens[i], message,link_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id,access_token,message,link_url):
    import requests
    
    url = f"https://graph.facebook.com/{page_id}/feed"
    params = {
        'message': message,
        'access_token': access_token,
        'link':link_url
    }
    
    response = requests.post(url, params=params)
    return response.json()  # Returns the response from the Facebook API


# ***************************SIMPLY COUNSEL*******************************#


class Text_post_to_simplycounsel_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = SimplyCounsel.objects.all().values('content','fb_page_id','fb_page_access_token','link_url')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = f"Content: {post['content']}"
                link_url = post['link_url']
               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i], access_tokens[i], message,link_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message,link_url):
    import requests
    
    url = f"https://graph.facebook.com/{page_id}/feed"
    params = {
        'message': message,
        'access_token': access_token,
        'link':link_url
    }
    
    response = requests.post(url, params=params)
    return response.json()  # Returns the response from the Facebook API

class Image_post_to_simplycounsel_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts=SimplyCounsel.objects.all().values('content','fb_page_id','fb_page_access_token','image_url')  # Fetch necessary fields
        print(posts)  
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  image_url = post['image_url']
                http_url=post['image_url']
                response = requests.head(http_url, allow_redirects=True)
                image_url = response.url
               #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"


               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i],access_tokens[i],message,image_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message, image_url):
    import requests
    
    upload_url = f"https://graph.facebook.com/v17.0/{page_id}/photos"
    params = {
        'message': message,
        'access_token': access_token,
        'url':image_url,
    }
    
    response = requests.post(upload_url,params=params)
    return response.json()  # Returns the response from the Facebook API

class Video_post_to_simplycounsel_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = SimplyCounsel.objects.all().values('content','fb_page_id','fb_page_access_token','video_url')  # Fetch necessary fields
        print(posts)
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  image_url = post['image_url']
                http_url=post['video_url']
                response = requests.head(http_url, allow_redirects=True)
                video_url = response.url
               #  video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_4.mp4"
               #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"


               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i],access_tokens[i],message,video_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message,video_url):
    import requests
    
    video_response = requests.post(f'https://graph-video.facebook.com/{page_id}/videos',
              files={'source': video_url},
                # files={'source': open('d:\Global Project\connectifyindia\public\media\short_video1.mp4', 'rb')},

         params={
            'access_token':access_token,
            'description':message
            }
            )
    if video_response.status_code == 200:
           video_id = video_response.json()['id']
           post_response = requests.post(
            f'https://graph.facebook.com/{page_id}/feed',
           params={
                'description':message,
                'attached_media[0]': f'{{"media_fbid":"{video_id}"}}',
                'access_token': access_token,
            }
           )
    if video_response.status_code == 200:
            print(f"Posted to Facebook Page {page_id} successfully.")
    else:
            print(f"Failed to post on page {page_id}: {video_response.text}")

class Link_post_to_simplycounsel_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = SimplyCounsel.objects.all().values('content','fb_page_id','fb_page_access_token','link_url')  # Fetch necessary fields
        print(posts)

        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
                link_url = post['link_url']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i], access_tokens[i], message,link_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id,access_token,message,link_url):
    import requests
    
    url = f"https://graph.facebook.com/{page_id}/feed"
    params = {
        'message': message,
        'access_token': access_token,
        'link':link_url
    }
    
    response = requests.post(url, params=params)
    return response.json()  # Returns the response from the Facebook API


# ***************************LEGAL ASPIRE*******************************#


class Text_post_to_legalaspire_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = LegalAspire.objects.all().values('content','fb_page_id','fb_page_access_token','link_url')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = f"Content: {post['content']}"
                link_url = post['link_url']
               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i], access_tokens[i],message,link_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message,link_url):
    import requests
    
    url = f"https://graph.facebook.com/{page_id}/feed"
    params = {
        'message': message,
        'access_token': access_token,
        'link':link_url
    }
    
    response = requests.post(url, params=params)
    return response.json()  # Returns the response from the Facebook API

class Image_post_to_legalaspire_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = LegalAspire.objects.all().values('content','fb_page_id','fb_page_access_token','image_url')  # Fetch necessary fields
        print(posts)
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  image_url = post['image_url']
                http_url=post['image_url']
                response = requests.head(http_url, allow_redirects=True)
                image_url = response.url
               #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"


               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i],access_tokens[i],message,image_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message, image_url):
    import requests
    
    upload_url = f"https://graph.facebook.com/v17.0/{page_id}/photos"
    params = {
        'message': message,
        'access_token': access_token,
        'url':image_url,
    }
    
    response = requests.post(upload_url,params=params)
    return response.json()  # Returns the response from the Facebook API

class Video_post_to_legalaspire_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = LegalAspire.objects.all().values('content','fb_page_id','fb_page_access_token','image_url')  # Fetch necessary fields
        print(posts)
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  image_url = post['image_url']
                http_url=post['video_url']
                response = requests.head(http_url, allow_redirects=True)
                video_url = response.url
               #  video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_4.mp4"
               #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"


               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i],access_tokens[i],message,video_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message,video_url):
    import requests
    
    video_response = requests.post(f'https://graph-video.facebook.com/{page_id}/videos',
              files={'source': video_url},
                # files={'source': open('d:\Global Project\connectifyindia\public\media\short_video1.mp4', 'rb')},

         params={
            'access_token':access_token,
            'description':message
            }
            )
    if video_response.status_code == 200:
           video_id = video_response.json()['id']
           post_response = requests.post(
            f'https://graph.facebook.com/{page_id}/feed',
           params={
                'description':message,
                'attached_media[0]': f'{{"media_fbid":"{video_id}"}}',
                'access_token': access_token,
            }
           )
    if video_response.status_code == 200:
            print(f"Posted to Facebook Page {page_id} successfully.")
    else:
            print(f"Failed to post on page {page_id}: {video_response.text}")

class Link_post_to_legalaspire_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = LegalAspire.objects.all().values('content','fb_page_id','fb_page_access_token','link_url')  # Fetch necessary fields
        print(posts)

        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
                link_url = post['link_url']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i], access_tokens[i], message,link_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id,access_token,message,link_url):
    import requests
    
    url = f"https://graph.facebook.com/{page_id}/feed"
    params = {
        'message': message,
        'access_token': access_token,
        'link':link_url
    }
    
    response = requests.post(url, params=params)
    return response.json()  # Returns the response from the Facebook API


    # ***************************AINAW*******************************#


class Text_post_to_ainaw_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = Ainaw.objects.all().values('content','fb_page_id','fb_page_access_token','link_url')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = f"Content: {post['content']}"
                link_url =post['link_url']

               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i], access_tokens[i], message,link_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token,message,link_url):
    import requests
    
    url = f"https://graph.facebook.com/{page_id}/feed"
    params = {
        'message': message,
        'access_token': access_token,
        'link':link_url
    }
    
    response = requests.post(url, params=params)
    return response.json()  # Returns the response from the Facebook API

class Image_post_to_ainaw_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = Ainaw.objects.all().values('content','fb_page_id','fb_page_access_token','image_url')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  image_url = post['image_url']
                http_url=post['image_url']
                response = requests.head(http_url, allow_redirects=True)
                image_url = response.url
                # image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"


               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i],access_tokens[i],message,image_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message, image_url):
    import requests
    
    upload_url = f"https://graph.facebook.com/v17.0/{page_id}/photos"
    params = {
        'message': message,
        'access_token': access_token,
        'url':image_url,
    }
    
    response = requests.post(upload_url,params=params)
    return response.json()  # Returns the response from the Facebook API

class Video_post_to_ainaw_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = Ainaw.objects.all().values('content','fb_page_id','fb_page_access_token','video_url')  # Fetch necessary fields
        print(posts)
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  image_url = post['image_url']
                http_url=post['video_url']
                response = requests.head(http_url, allow_redirects=True)
                video_url = response.url
               #  video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_4.mp4"
               #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
                # video_url="d:\Global Project\connectifyindia\public\media\Connectify India Company Service details.mp4"


               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i],access_tokens[i],message,video_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id,access_token,message,video_url):
    import requests
    
    video_response = requests.post(f'https://graph-video.facebook.com/{page_id}/videos',
              files={'source': video_url},
               #  files={'source': open('d:\Global Project\connectifyindia\public\media\short_video1.mp4', 'rb')},
               # files={'source': open(f'{video_url}', 'rb')},

         params={
            'access_token':access_token,
            'description':message
            }
            )
    if video_response.status_code == 200:
           video_id = video_response.json()['id']
           post_response = requests.post(
            f'https://graph.facebook.com/{page_id}/feed',
           params={
                'description':message,
                'attached_media[0]': f'{{"media_fbid":"{video_id}"}}',
                'access_token': access_token,
            }
           )
    if video_response.status_code==200:
            print(f"Posted to Facebook Page {page_id} successfully.")
    else:
            print(f"Failed to post on page {page_id}:{video_response.text}")

class Link_post_to_ainaw_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = Ainaw.objects.all().values('content','fb_page_id','fb_page_access_token','link_url')  # Fetch necessary fields
        print(posts)

        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
                link_url = post['link_url']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i], access_tokens[i],message,link_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id,access_token,message,link_url):
    import requests
    url = f"https://graph.facebook.com/{page_id}/feed"
    params = {
        'message': message,
        'access_token': access_token,
        'link':link_url
    }
    
    response = requests.post(url, params=params)
    return response.json()  # Returns the response from the Facebook API


# ************************BUSINESS CONNECT*************************************


class Text_post_to_businessconnect_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = BusinessConnect.objects.all().values('content','fb_page_id','fb_page_access_token')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = f"Content: {post['content']}"
               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i], access_tokens[i], message)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message):
    import requests
    
    url = f"https://graph.facebook.com/{page_id}/feed"
    params = {
        'message': message,
        'access_token': access_token
    }
    
    response = requests.post(url, params=params)
    return response.json()  # Returns the response from the Facebook API

class Image_post_to_businessconnect_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = BusinessConnect.objects.all().values('content','fb_page_id','fb_page_access_token','image_url')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  image_url = post['image_url']
                http_url=post['image_url']
                response = requests.head(http_url, allow_redirects=True)
                image_url = response.url
               #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"


               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i],access_tokens[i],message,image_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message, image_url):
    import requests
    
    upload_url = f"https://graph.facebook.com/v17.0/{page_id}/photos"
    params = {
        'message': message,
        'access_token': access_token,
        'url':image_url,
    }
    
    response = requests.post(upload_url,params=params)
    return response.json()  # Returns the response from the Facebook API

class Video_post_to_businessconnect_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = BusinessConnect.objects.all().values('content','fb_page_id','fb_page_access_token','video_url')  # Fetch necessary fields
        print(posts)
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  image_url = post['image_url']
                http_url=post['video_url']
                response = requests.head(http_url, allow_redirects=True)
                video_url = response.url
               #  video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_4.mp4"
               #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"


               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i],access_tokens[i],message,video_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id, access_token, message,video_url):
    import requests
    
    video_response = requests.post(f'https://graph-video.facebook.com/{page_id}/videos',
              files={'source': video_url},
                # files={'source': open('d:\Global Project\connectifyindia\public\media\short_video1.mp4', 'rb')},

         params={
            'access_token':access_token,
            'description':message
            }
            )
    if video_response.status_code == 200:
           video_id = video_response.json()['id']
           post_response = requests.post(
            f'https://graph.facebook.com/{page_id}/feed',
           params={
                'description':message,
                'attached_media[0]': f'{{"media_fbid":"{video_id}"}}',
                'access_token': access_token,
            }
           )
    if video_response.status_code == 200:
            print(f"Posted to Facebook Page {page_id} successfully.")
    else:
            print(f"Failed to post on page {page_id}: {video_response.text}")

class Link_post_to_businessconnect_page(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = BusinessConnect.objects.all().values('content','fb_page_id','fb_page_access_token','link_url')  # Fetch necessary fields
        print(posts)

        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
                link_url = post['link_url']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_facebook(page_ids[i], access_tokens[i], message,link_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Facebook."})

# Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id,access_token,message,link_url):
    import requests
    
    url = f"https://graph.facebook.com/{page_id}/feed"
    params = {
        'message': message,
        'access_token': access_token,
        'link':link_url
    }
    
    response = requests.post(url, params=params)
    return response.json()  # Returns the response from the Facebook API


# **********************************INSTAGRAM************************************

class Image_post_to_instagram(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = Instagram.objects.all().values('content','fb_page_id','fb_page_access_token','image_url','instagram_user_id')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]
            key_to_extract3 = 'instagram_user_id'
            ig_user_id = [d[key_to_extract3] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  image_url = post['image_url']
                # http_url=post['image_url']
                # response = requests.head(http_url, allow_redirects=True)
                # image_url = response.url
                image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"



               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_instagram(access_tokens[i],message,image_url,ig_user_id)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Instagram"})

# Function to post to Facebook using the Facebook Graph API
def post_to_instagram(access_token, message, image_url,ig_user_id):
    import requests
    import json
    payload={
        'caption':message,
        'access_token':access_token,
        'image_url':image_url
    }
    response=requests.post('https://graph.facebook.com/v17.0/{}/media'.format(ig_user_id),data=payload)
    print(response.text)
    print("Media Uploaded Successfully")
    results=json.loads(response.text)
    if 'id' in results:
        creation_id=results['id']
        second_url='https://graph.facebook.com/v17.0/{}/media_publish'.format(ig_user_id)
        second_payload={
           'creation_id':creation_id,
           'access_token':access_token
        }
        response=requests.post(second_url,data=second_payload)
        if response.status_code==200:
           print("image published to instagram")
        else:
           print("image posting is not possible")


class Video_post_to_instagram(APIView):
    def get(self,request):
        # Retrieve data from the database (e.g., Post model)
        posts = Instagram.objects.all().values('content','fb_page_id','fb_page_access_token','video_url','instagram_user_id')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'fb_page_id'
            page_ids = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'fb_page_access_token'
            access_tokens = [d[key_to_extract2] for d in posts]

            key_to_extract3 = 'instagram_user_id'
            ig_user_id = [d[key_to_extract3] for d in posts]
            # access_tokens="EAAEafQqhaTgBO5yxkplfLOogg9U9Wev8MEqwW6Mhm5RJ5DrluVresl1743Ktf7C31K8wYo1ZCj4QMq6wZBQAs7b2RijJEKjWYECZBQp0FpGZAYa6RVZBrZBy9sB3b3wsDTaxr9PPgyea0jpMZBA5YdXF7flUMPYX0LhgHfGYN2pokMuAsQZAtKi6iv10QirHkNouOONtHJDn6chDW4hjcjZCRrorxuJPnpScQAlKI3WEZD"
            # ig_user_id="17841431996866861"
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  image_url = post['image_url']
                # http_url=post['video_url']
                # response = requests.head(http_url, allow_redirects=True)
                # video_url = response.url
               #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
                # video_url="https://connectifyindiasqldb.azurewebsites.net/media/videoplayback_4.mp4"



               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(page_ids)):
                    response = post_to_instagram(page_ids[i],access_tokens[i],message,ig_user_id)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Instagram"})

# Function to post to Facebook using the Facebook Graph API
def post_to_instagram(page_id,access_token,message,ig_user_id):
    import requests
    import json
    import time
    video_url="https://connectifyindiasqldb.azurewebsites.net/media/videoplayback_4.mp4"
    payload={
         'caption':message,
         'access_token':access_token,
         'media_type': 'VIDEO',
         'video_url':video_url
        }
    response=requests.post('https://graph.facebook.com/v17.0/{}/media'.format(ig_user_id),data=payload)
    print(response.text)
    print("Media Uploaded Successfully")
    time.sleep(30)
    results=json.loads(response.text)
    if 'id' in results:
         creation_id=results['id']
        #  print(creation_id)
         status_url = f"https://graph.facebook.com/v17.0/{creation_id}?fields=status&access_token={access_token}"
         
         while True:
           status_response = requests.get(status_url)

           try:
             status_data = status_response.json()
             media_status = status_data.get('status')
           except json.JSONDecodeError:
             print("Failed to decode JSON response. Retrying...")
             time.sleep(10)  # Wait for 10 seconds before retrying
             continue
           
           second_url='https://graph.facebook.com/v17.0/{}/media_publish'.format(ig_user_id)
           second_payload={
              'creation_id':creation_id,
              'access_token':access_token
             }
           response=requests.post(second_url,data=second_payload)
           if response.status_code == 200:
              print("Video successfully published!")
              break
           else:
              print("Failed to publish the video:")


# *******************************WHATSAPP**************************************
    # recepient_number=models.CharField(max_length=15,null=True,blank=True)
    # phone_number_id=models.CharField(max_length=100,null=True,blank=True)
    # WhatsApp_Business_Account_ID=models.CharField(max_length=100,null=True,blank=True)
    # auth_token=models.CharField(max_length=500)
    # city_name=models.CharField(max_length=100,null=True,blank=True)
    # address=models.TextField(null=True,blank=True)
    # longitude=models.CharField(max_length=100,null=True,blank=True)
    # latitude=models.CharField(max_length=100,null=True,blank=True)

class Text_post_to_whatsapp(APIView):
    def get(request,format=None):
        # Retrieve data from the database (e.g., Post model)
        posts = Whatsapp.objects.all().values('recepient_number','phone_number_id','auth_token','content')  # Fetch necessary fields
        # print(posts)
        
        if posts: 
            key_to_extract1 = 'recepient_number'
            recepient_number = [d[key_to_extract1] for d in posts]
            # print(recepient_number)
            key_to_extract2 = 'phone_number_id'
            phone_number_id = [d[key_to_extract2] for d in posts]
            # key_to_extract3 = 'WhatsApp_Business_Account_ID'
            # WhatsApp_Business_Account_ID = [d[key_to_extract3] for d in posts]
            key_to_extract4 = 'auth_token'
            auth_token = [d[key_to_extract4] for d in posts]
            # print(auth_token)
            # key_to_extract5 = 'content'
            # content = [d[key_to_extract5] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
               #  page_ids = post['fb_page_id']
               #  access_tokens = str(post['fb_page_access_token'])
                # Post on each Facebook page
                print(len(recepient_number))
                for i in range(len(recepient_number)):
                    response = post_to_whatsapp(recepient_number[i], phone_number_id[i],auth_token[i],message)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on whatsapp."})

# Function to post to Facebook using the Facebook Graph API
def post_to_whatsapp(recepient_number,phone_number_id,auth_token,message):
    import requests
    post_url=f"https://graph.facebook.com/v18.0/{phone_number_id}/messages"
      # Construct the payload
    payload = {
         "messaging_product": "whatsapp",
         "recipient_type": "individual",
         "to": recepient_number,
         "type": "template",
        #  "text": {
        #    "preview_url": False,
        #    "body": message
        #  },
         
         "template": {
             "name": "hello_world",
             "language": {
                "code": "en_US"
              }
    }
}

# Headers with authentication token
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
        }

# Send the POST request
    response = requests.post(post_url,json=payload,headers=headers)

    if response.status_code == 200:
         print("Message sent successfully!")
         print(response.text)
    else:
         print("Failed to send message:", response.text)


class Image_post_to_whatsapp(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = Whatsapp.objects.all().values('recepient_number','phone_number_id','auth_token','content','image_url')  # Fetch necessary fields
        print(posts) 
        if posts: 
            key_to_extract1 = 'recepient_number'
            recepient_number = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'phone_number_id'
            phone_number_id = [d[key_to_extract2] for d in posts]
            # key_to_extract3 = 'WhatsApp_Business_Account_ID'
            # WhatsApp_Business_Account_ID = [d[key_to_extract3] for d in posts]
            key_to_extract4 = 'auth_token'
            auth_token = [d[key_to_extract4] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                # message = f"Content: {post['content']}"
                # image_url = post['image_url']
                # print(image_url)
                image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"

               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(recepient_number)):
                    response = post_to_whatsapp(recepient_number[i], phone_number_id[i],auth_token[i],image_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Whatsapp."})

# Function to post to Facebook using the Facebook Graph API
def post_to_whatsapp(recepient_number,phone_number_id,auth_token,image_url):
    import requests
    post_url=f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"
    payload = {
        "recipient_type": "individual",
        "to": recepient_number,
        # "to": 917519526081,
        "type": "image",
        "image": {
        "link": image_url
        },
        "messaging_product": "whatsapp",
}
# Headers with authentication token
    headers = {
         "Authorization": f"Bearer {auth_token}",
         "Content-Type": "application/json"
         }
       

# Send the POST request
    response = requests.post(post_url,json=payload,headers=headers)
    print(response.text)
    if response.status_code == 200:
         print("Message sent successfully!")
         print(response.text)
    else:
        print("Failed to send message:", response.text)


class Video_post_to_whatsapp(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = Whatsapp.objects.all().values('recepient_number','phone_number_id','auth_token','content','video_url')  # Fetch necessary fields
        print(posts) 
        if posts: 
            key_to_extract1 = 'recepient_number'
            recepient_number = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'phone_number_id'
            phone_number_id = [d[key_to_extract2] for d in posts]
            # key_to_extract3 = 'WhatsApp_Business_Account_ID'
            # WhatsApp_Business_Account_ID = [d[key_to_extract3] for d in posts]
            key_to_extract4 = 'auth_token'
            auth_token = [d[key_to_extract4] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                # message = f"Content: {post['content']}"
                # video_url = post['video_url']
                # print(video_url)
                # image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
                video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_3.mp4"

               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(recepient_number)):
                    response = post_to_whatsapp(recepient_number[i], phone_number_id[i],auth_token[i],video_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Whatsapp."})

# Function to post to Facebook using the Facebook Graph API
def post_to_whatsapp(recepient_number,phone_number_id,auth_token,video_url):
    import requests
    post_url=f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"
    payload = {
        "recipient_type": "individual",
        "to": recepient_number,
        # "to": 917519526081,
        "type": "video",
        "video": {
        "link": video_url
        },
        "messaging_product": "whatsapp",
}
# Headers with authentication token
    headers = {
         "Authorization": f"Bearer {auth_token}",
         "Content-Type": "application/json"
         }
       

# Send the POST request
    response = requests.post(post_url,json=payload,headers=headers)
    print(response.text)
    if response.status_code == 200:
         print("Message sent successfully!")
         print(response.text)
    else:
        print("Failed to send message:", response.text)

class Location_post_to_whatsapp(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = Whatsapp.objects.all().values('recepient_number','phone_number_id','auth_token','content','city_name','address','longitude','latitude')  # Fetch necessary fields
        print(posts) 
        if posts: 
            key_to_extract1 = 'recepient_number'
            recepient_number = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'phone_number_id'
            phone_number_id = [d[key_to_extract2] for d in posts]
            # key_to_extract3 = 'WhatsApp_Business_Account_ID'
            # WhatsApp_Business_Account_ID = [d[key_to_extract3] for d in posts]
            key_to_extract4 = 'auth_token'
            auth_token = [d[key_to_extract4] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                # message = f"Content: {post['content']}"
                # video_url = post['video_url']
                # print(video_url)
                # image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
                # video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_3.mp4"
                city_name = post['city_name']
                address=post['address']
                longitude=post['longitude']
                latitude=post['latitude']

               #  page_ids = post['fb_page_id']
               
               #  access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
                for i in range(len(recepient_number)):
                    response = post_to_whatsapp(recepient_number[i], phone_number_id[i],auth_token[i],city_name,address,longitude,latitude)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Whatsapp."})

# Function to post to Facebook using the Facebook Graph API
def post_to_whatsapp(recepient_number,phone_number_id,auth_token,city_name,address,longitude,latitude):
    import requests
    post_url=f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"
    payload = {
         "recipient_type": "individual",
         "to": recepient_number,
         "type": "location",
         "location": {
         "longitude":longitude,
         "latitude":latitude,
         "name": city_name,
         "address": address
         },
         "messaging_product": "whatsapp",
}
# Headers with authentication token
    headers = {
         "Authorization": f"Bearer {auth_token}",
         "Content-Type": "application/json"
         }
       

# Send the POST request
    response = requests.post(post_url,json=payload,headers=headers)
    print(response.text)
    if response.status_code == 200:
         print("Message sent successfully!")
         print(response.text)
    else:
        print("Failed to send message:", response.text)


# class Document_post_to_whatsapp(APIView):
#     def get(self, request):
#         # Retrieve data from the database (e.g., Post model)
#         posts = Whatsapp.objects.all().values('recepient_number','phone_number_id','auth_token','document')  # Fetch necessary fields
#         print(posts) 
#         if posts: 
#             key_to_extract1 = 'recepient_number'
#             recepient_number = [d[key_to_extract1] for d in posts]
#             key_to_extract2 = 'phone_number_id'
#             phone_number_id = [d[key_to_extract2] for d in posts]
#             # key_to_extract3 = 'WhatsApp_Business_Account_ID'
#             # WhatsApp_Business_Account_ID = [d[key_to_extract3] for d in posts]
#             key_to_extract4 = 'auth_token'
#             auth_token = [d[key_to_extract4] for d in posts]
#             for post in posts:
#                 # Customize the message content here using the retrieved data
#                 # message = f"Content: {post['content']}"
#                 # video_url = post['video_url']
#                 # print(video_url)
#                 # image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
#                 # video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_3.mp4"
#                 # document=post['document']
#                 document="http://connectifyindiasqldb.azurewebsites.net/media/LegalAspire.xlsx"

#                #  page_ids = post['fb_page_id']
               
#                #  access_tokens = str(post['fb_page_access_token'])
           
#                 # Post on each Facebook page
#                 for i in range(len(recepient_number)):
#                     response = post_to_whatsapp(recepient_number[i], phone_number_id[i],auth_token[i],document)
#                     print(response)  # Print the response from the Facebook API

#         return Response({"message": "Data fetched from the database and posted on Whatsapp."})

# # Function to post to Facebook using the Facebook Graph API
# def post_to_whatsapp(recepient_number,phone_number_id,auth_token,document):
#     import requests
#     post_url=f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"
#     payload = {
#          "recipient_type": "individual",
#          "to": recepient_number,
#          "type": "document",
#          "document": {
#           "link":document
#          },
#          "messaging_product": "whatsapp",
# }
# # Headers with authentication token
#     headers = {
#          "Authorization": f"Bearer {auth_token}",
#          "Content-Type": "application/json"
#          }
       

# # Send the POST request
#     response = requests.post(post_url,json=payload,headers=headers)
#     print(response.text)
#     if response.status_code == 200:
#          print("Message sent successfully!")
#          print(response.text)
#     else:
#         print("Failed to send message:", response.text)


class Text_post_to_telegram(APIView):
    def get(self,request):
        # Retrieve data from the database (e.g., Post model)
        posts = Telegram.objects.all().values('content','chat_id','bot_token')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'chat_id'
            chat_id = [d[key_to_extract1] for d in posts]
            # print(chat_id)
            key_to_extract2 = 'bot_token'
            bot_token = [d[key_to_extract2] for d in posts]
            # print(bot_token)
            for post in posts:
                # Customize the message content here using the retrieved data
                 msg=post['content']
           
                # Post on each Facebook page
                 for i in range(len(chat_id)):
                    response = post_to_telegram(chat_id[i],bot_token[i],msg)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on telegram."})

# Function to post to Facebook using the Facebook Graph API
def post_to_telegram(chat_id,bot_token,msg):
    import requests
    params = {
       'chat_id':chat_id,
       'text': msg
      }
    try:
    # Send the message
        response =requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage',params=params)
        response.raise_for_status()
        print('Message sent successfully!')
    except requests.exceptions.HTTPError as e:
        print(f'Error sending message: {e}')

class Image_post_to_telegram(APIView):
    def get(self,request):
        # Retrieve data from the database (e.g., Post model)
        posts = Telegram.objects.all().values('content','chat_id','bot_token','image_url')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'chat_id'
            chat_id = [d[key_to_extract1] for d in posts]
            print(chat_id)
            key_to_extract2 = 'bot_token'
            bot_token = [d[key_to_extract2] for d in posts]
            print(bot_token)
            for post in posts:
                # Customize the message content here using the retrieved data
                 msg=post['content']
                #  image_url=post['image_url']
                 image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"


           
                # Post on each Facebook page
                 for i in range(len(chat_id)):
                    response = post_to_telegram(chat_id[i],bot_token[i],msg,image_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on telegram."})

# Function to post to Facebook using the Facebook Graph API
def post_to_telegram(chat_id,bot_token,msg,image_url):
    import requests
    image_params = {
       'chat_id': chat_id,
       'photo':image_url,
       'caption':msg
       }
    try:
        response = requests.post(f'https://api.telegram.org/bot{bot_token}/sendPhoto', params=image_params)
        response.raise_for_status()
        print('Image sent successfully!')
    except requests.exceptions.HTTPError as e:
        print(f'Error sending image: {e}')


class Video_post_to_telegram(APIView):
    def get(self,request):
        # Retrieve data from the database (e.g., Post model)
        posts = Telegram.objects.all().values('content','chat_id','bot_token','video_url')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'chat_id'
            chat_id = [d[key_to_extract1] for d in posts]
            # print(chat_id)
            key_to_extract2 = 'bot_token'
            bot_token = [d[key_to_extract2] for d in posts]
            # print(bot_token)
            for post in posts:
                # Customize the message content here using the retrieved data
                 msg=post['content']
                #  video_url=post['video_url']

                #  image_url=post['image_url']
                #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
                 video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_3.mp4"


           
                # Post on each Facebook page
                 for i in range(len(chat_id)):
                    response = post_to_telegram(chat_id[i],bot_token[i],msg,video_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on telegram."})

# Function to post to Facebook using the Facebook Graph API
def post_to_telegram(chat_id,bot_token,msg,video_url):
    import requests
    video_message_params = {
       'chat_id': chat_id,
       'video': video_url,
       'caption':msg
       }
    try:
        # Send the video message
         response = requests.post(f'https://api.telegram.org/bot{bot_token}/sendVideo', params=video_message_params)
         response.raise_for_status()
         print('Video sent successfully!')
    except requests.exceptions.HTTPError as e:
         print(f'Error sending video: {e}')


class Document_post_to_telegram(APIView):
    def get(self,request):
        # Retrieve data from the database (e.g., Post model)
        posts = Telegram.objects.all().values('content','chat_id','bot_token','document')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'chat_id'
            chat_id = [d[key_to_extract1] for d in posts]
            # print(chat_id)
            key_to_extract2 = 'bot_token'
            bot_token = [d[key_to_extract2] for d in posts]
            # print(bot_token)
            for post in posts:
                # Customize the message content here using the retrieved data
                 msg=post['content']
                #  document=post['document']
                 document="https://www.vssut.ac.in/lecture_notes/lecture1423726024.pdf"

                #  video_url=post['video_url']

                #  image_url=post['image_url']
                #  image_url="https://www.esamskriti.com/essays/docfile/8_6742.jpg"
                #  video_url="http://connectifyindiasqldb.azurewebsites.net/media/videoplayback_3.mp4"


           
                # Post on each Facebook page
                 for i in range(len(chat_id)):
                    response = post_to_telegram(chat_id[i],bot_token[i],msg,document)
                    print(response)  # Print the response from the Facebook API

        return Response({"message":"Data fetched from the database and posted on telegram."})

# Function to post to Facebook using the Facebook Graph API
def post_to_telegram(chat_id,bot_token,msg,document):
    import requests
    document_message_params = {
        'chat_id': chat_id,
        'document': document,
        'caption':msg
        }
      
    try:
        # Send the video message
         response = requests.post(f'https://api.telegram.org/bot{bot_token}/sendDocument', params=document_message_params)
         response.raise_for_status()
         print('Document sent successfully!')

    except requests.exceptions.HTTPError as e:
         print(f'Error sending Document: {e}')


class Article_post_to_linkedin(APIView):
    def get(self,request):
        # Retrieve data from the database (e.g., Post model)
        posts = Linkedln.objects.all().values('content','link_url','thumbnail_url','linkedln_person_urn','access_token')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1='linkedln_person_urn'
            urn_id = [d[key_to_extract1] for d in posts]
            # print(chat_id)
            key_to_extract2='access_token'
            access_token=[d[key_to_extract2] for d in posts]
            # print(access_token)
            for post in posts:
                # Customize the message content here using the retrieved data
                 msg=post['content']
                 originalUrl=post['link_url']
                 thumbnail_url=post['thumbnail_url']
           
                # Post on each Facebook page
                 for i in range(len(urn_id)):
                    response = post_to_telegram(urn_id[i],access_token[i],msg,originalUrl,thumbnail_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Linkedin."})

# Function to post to Facebook using the Facebook Graph API
def post_to_telegram(urn_id,access_token,msg,originalUrl,thumbnail_url):
    import requests
    POST_URL = 'https://api.linkedin.com/v2/ugcPosts'
# text="""
# The example below creates a simple text Share on LinkedIn.Notice the visibility is set to PUBLIC, where anyone on the LinkedIn Platform can view this share.
# """
    headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'x-li-format': 'json'
        }

    post_data = {
            'author': f'urn:li:person:{urn_id}',
            'lifecycleState':'PUBLISHED',
            'visibility': {
                'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'
            },
            'specificContent': {
                'com.linkedin.ugc.ShareContent': {
                    'shareCommentary': {
                        'text': msg
                    },
                    "shareMediaCategory": "ARTICLE",
                    "media": [
                        {
                            "status": "READY",
                            "description": {
                                "text": "Official LinkedIn Blog - Your source for insights and information about LinkedIn."
                            },
                            "originalUrl":originalUrl,
                            "title": {
                                "text": "Official LinkedIn Blog"
                            },
                            "thumbnails":[{
                            "url":thumbnail_url
                    }]
                        }
                    ]
                }
            }
        }

    response = requests.post(POST_URL,headers=headers,json=post_data)
    if response.status_code == 201:
            print('Successfully posted on LinkedIn.',response.text)
    else:
            print('Error posting on LinkedIn:',response.status_code,response.text)


class Image_post_to_linkedin(APIView):
    def get(self,request):
        # Retrieve data from the database (e.g., Post model)
        posts = Linkedln.objects.all().values('content','linkedln_person_urn','access_token','image_url')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'linkedln_person_urn'
            urn_id = [d[key_to_extract1] for d in posts]
            # print(chat_id)
            key_to_extract2 = 'access_token'
            access_token = [d[key_to_extract2] for d in posts]
            # print(access_token)
            for post in posts:
                # Customize the message content here using the retrieved data
                 msg=post['content']
                #  http_url=post['image_url']
                #  response = requests.head(http_url,allow_redirects=True)
                #  image_url = response.url
                 image_url = 'http://www.esamskriti.com/essays/docfile/8_6742.jpg'  # Replace with the actual URL of your image

           
                # Post on each Facebook page
                 for i in range(len(urn_id)):
                    response = post_to_telegram(urn_id[i],access_token[i],msg,image_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Linkedin."})

# Function to post to Facebook using the Facebook Graph API
def post_to_telegram(urn_id,access_token,msg,image_url):
    import requests
    MEDIA_UPLOAD_URL ='https://api.linkedin.com/v2/assets?action=registerUpload'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        "X-Restli-Protocol-Version": "2.0.0"
        }

    media_data = {
        'registerUploadRequest': {
        'owner':f'urn:li:person:{urn_id}',
        'recipes': ['urn:li:digitalmediaRecipe:feedshare-image'],
        'serviceRelationships': [
            {
                'relationshipType': 'OWNER',
                'identifier': 'urn:li:userGeneratedContent'
            }
            ]
           }
        }
      

    response1 = requests.post(MEDIA_UPLOAD_URL,headers=headers,json=media_data)
    print(response1.status_code)
    print("******************************************************")
    result=json.loads(response1.text)
    print(result)
    uploadUrl=response1.json()['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest'][
        'uploadUrl']
      #  print(uploadUrl)

# ********************************************************************************************
    headers1 = {
          'Authorization': f'Bearer {access_token}',
          "media-type-family": "STILLIMAGE",
          "Content-Type": "image/png"
        }
      #  with open(image_url,'rb') as f:
      #    data = f.read()
    response = requests.post(uploadUrl,headers=headers1,data=image_url)
    print(response.status_code)
    print(response.text)
# ********************************************************************************************

    if response1.status_code == 200:
          media_urn= response1.json()['value']['asset']
          print(media_urn)
    else:
           print('Error uploading media:', response.status_code, response.text)


# **************************************************************************************************

    SHARE_URL = 'https://api.linkedin.com/v2/ugcPosts'

    share_data = {
         "author": f"urn:li:person:{urn_id}",
         "lifecycleState": "PUBLISHED",
         "specificContent": {
         "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text":msg
            },
            "shareMediaCategory": "IMAGE",
            "media": [
                {
                    "status": "READY",
                    "description": {
                        "text":msg 
                    },
                    "media":media_urn,
                    "title": {
                        "text": "create linkdln profile"
                    }
                }
            ]
           }
          },
          "visibility": {
          "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
          }
          }
# print(media_urn)
    response = requests.post(SHARE_URL, headers=headers,json=share_data)
    print(response.status_code)
    print(response.text)
    if response.status_code == 201:
        print('Successfully posted on LinkedIn.')
    else:
        print('Error posting on LinkedIn:', response.status_code, response.text) 



class Video_post_to_linkedin(APIView):
    def get(self,request):
        # Retrieve data from the database (e.g., Post model)
        posts = Linkedln.objects.all().values('content','linkedln_person_urn','access_token','video_url')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'linkedln_person_urn'
            urn_id = [d[key_to_extract1] for d in posts]
            # print(chat_id)
            key_to_extract2 = 'access_token'
            access_token = [d[key_to_extract2] for d in posts]
            # print(access_token)
            for post in posts:
                # Customize the message content here using the retrieved data
                 msg=post['content']
                #  http_url=post['video_url']
                #  response = requests.head(http_url,allow_redirects=True)
                #  video_url = response.url
                 video_url="d:\Local Project\connectifyindia\public\media\short_video2.mp4"

           
                # Post on each Facebook page
                 for i in range(len(urn_id)):
                    response = post_to_telegram(urn_id[i],access_token[i],msg,video_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Linkedin."})

# Function to post to Facebook using the Facebook Graph API
def post_to_telegram(urn_id,access_token,msg,video_url):
    import requests
    headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
       }
    media_data = {
            "registerUploadRequest": {
                "recipes": ["urn:li:digitalmediaRecipe:feedshare-video"],
                "owner": f"urn:li:person:{urn_id}",
                "serviceRelationships": [
                    {
                        "relationshipType": "OWNER",
                        "identifier": "urn:li:userGeneratedContent",
                    }
                ],
            }
        }

    response1 = requests.post(
            "https://api.linkedin.com/v2/assets?action=registerUpload",
            headers=headers,
            json=media_data,
        )
    print(response1.status_code)
        # print("******************************************************")
    result = json.loads(response1.text)
    #    print("This is result:",result)
    uploadUrl = response1.json()["value"]["uploadMechanism"][
            "com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"
        ]["uploadUrl"]
        # ********************************************************************************************
    headers1 = {
            "Authorization": f"Bearer {access_token}",
            "media-type-family": "VIDEO",
        }
        # print(video_url)
    with open(video_url, "rb") as f:
            data = f.read()

    response = requests.post(uploadUrl, headers=headers1, data=data)
    print(response.status_code)
    print(response.text)
    time.sleep(30)
        # ********************************************************************************************

    if response1.status_code == 200:
            media_urn = response1.json()["value"]["asset"]
            print(media_urn)
    else:
        print("Error uploading media:", response.status_code, response.text)

        # **************************************************************************************************

    SHARE_URL = "https://api.linkedin.com/v2/ugcPosts"

    share_data = {
            "author": f"urn:li:person:{urn_id}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": msg},
                    "shareMediaCategory": "VIDEO",
                    "media": [
                       {
                            "status": "READY",
                            "description": {"text": "Center stage!"},
                            "media": media_urn,
                            "title": {"text": "LinkedIn Talent Connect 2023"},
                        }
                    ],
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
        }

    response = requests.post(SHARE_URL, headers=headers, json=share_data)
    print(response.text)
    if response.status_code == 201:
            print("Successfully posted on LinkedIn.")
    else:
            print("Error posting on LinkedIn:", response.status_code,response.text)



# Linkedln Group


class Article_post_to_linkedin_group(APIView):
    def get(self,request):
        # Retrieve data from the database (e.g., Post model)
        posts = Linkedln.objects.all().values('content','link_url','thumbnail_url','linkedln_person_urn','linkedln_group_urn','access_token')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'linkedln_person_urn'
            urn_id = [d[key_to_extract1] for d in posts]

            key_to_extract1 = 'linkedln_group_urn'
            group_urn_id = [d[key_to_extract1] for d in posts]

            key_to_extract2 = 'access_token'
            access_token = [d[key_to_extract2] for d in posts]
            # print(access_token)
            for post in posts:
                # Customize the message content here using the retrieved data
                 msg=post['content']
                 originalUrl=post['link_url']
                 thumbnail_url=post['thumbnail_url']
           
                # Post on each Facebook page
                 for i in range(len(urn_id)):
                    response = post_to_telegram(urn_id[i],group_urn_id[i],access_token[i],msg,originalUrl,thumbnail_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Linkedin."})

# Function to post to Facebook using the Facebook Graph API
def post_to_telegram(urn_id,group_urn_id,access_token,msg,originalUrl,thumbnail_url):
    import requests
    POST_URL = 'https://api.linkedin.com/v2/ugcPosts'

 
    headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'x-li-format': 'json'
        }

    post_data = {
            'author': f'urn:li:person:{urn_id}',
            'containerEntity':f'urn:li:group:{group_urn_id}',
            'lifecycleState': 'PUBLISHED',
            'visibility': {
                'com.linkedin.ugc.MemberNetworkVisibility': 'CONTAINER'
            },
            'specificContent': {
                'com.linkedin.ugc.ShareContent': {
                    'shareCommentary': {
                        'text': msg
                    },
                    "shareMediaCategory": "ARTICLE",
                    "media": [
                        {
                            "status": "READY",
                            "description": {
                                "text": "Welcome to Connectify India, your one-stop platform for all your career counseling, legal services, social service, and business needs. Our four verticals work towards connecting students, teachers, advocates, law students, interns, consumers, NGOs, and business owners across India."
                            },
                            "originalUrl": originalUrl,
                            "title": {
                                "text": "Connectify India Company Service details"
                            },
                            "thumbnails":[{
                                "url":thumbnail_url
                            }]
                        }
                    ]
                }
            }
        }

    response = requests.post(POST_URL, headers=headers, json=post_data)
    if response.status_code == 201:
            print('Successfully posted on LinkedIn.')
    else:
            print('Error posting on LinkedIn:', response.status_code, response.text)


class Image_post_to_linkedin_group(APIView):
    def get(self,request):
        # Retrieve data from the database (e.g., Post model)
        posts = Linkedln.objects.all().values('content','linkedln_person_urn','linkedln_group_urn','access_token','image_url')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'linkedln_person_urn'
            urn_id = [d[key_to_extract1] for d in posts]
            # print(chat_id)
            key_to_extract1 = 'linkedln_group_urn'
            group_urn_id = [d[key_to_extract1] for d in posts]

            key_to_extract2 = 'access_token'
            access_token = [d[key_to_extract2] for d in posts]
            # print(access_token)
            for post in posts:
                # Customize the message content here using the retrieved data
                 msg=post['content']
                 http_url=post['image_url']
                 response = requests.head(http_url,allow_redirects=True)
                 image_url = response.url
           
                # Post on each Facebook page
                 for i in range(len(urn_id)):
                    response = post_to_telegram(urn_id[i],group_urn_id[i],access_token[i],msg,image_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Linkedin."})

# Function to post to Facebook using the Facebook Graph API
def post_to_telegram(urn_id,group_urn_id,access_token,msg,image_url):
    import requests
    MEDIA_UPLOAD_URL = 'https://api.linkedin.com/v2/assets?action=registerUpload'
    headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

    media_data = {
            'registerUploadRequest': {
                'recipes': ['urn:li:digitalmediaRecipe:feedshare-image'],
                'owner': f'urn:li:person:{urn_id}',
                'serviceRelationships': [
                    {
                        'relationshipType': 'OWNER',
                        'identifier': 'urn:li:userGeneratedContent'
                    }
                ]
            }
        }

    response1 = requests.post(MEDIA_UPLOAD_URL, headers=headers, json=media_data)
    print(response1.status_code)
    print("******************************************************")
    result=json.loads(response1.text)
        # print(result)
    uploadUrl=response1.json()['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest'][
                'uploadUrl']
# print(uploadUrl)

# ********************************************************************************************
    headers1 = {
            'Authorization': f'Bearer {access_token}',
            'media-type-family': 'STILLIMAGE'
        }
    #    payload={
    #         'submitted-image-url':image_url
    #    }



    #    with open(image_url,'rb') as f:
    #         data = f.read()

    response = requests.post(uploadUrl,headers=headers1,data=image_url)
    print(response.status_code)
    print(response.text)
        # ********************************************************************************************

    if response1.status_code == 200:
            media_urn= response1.json()['value']['asset']
            # print(media_urn)
    else:
            print('Error uploading media:', response.status_code, response.text)


        # **************************************************************************************************

    SHARE_URL = 'https://api.linkedin.com/v2/ugcPosts'

    share_data = {
            "author": f"urn:li:person:{urn_id}",
            'containerEntity': f'urn:li:group:{group_urn_id}',
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": msg
                    },
                    "shareMediaCategory": "IMAGE",
                    "media": [
                        {
                            "status": "READY",
                            "description": {
                                "text": "Ganesha, the son of Lord Shiva and Devi Parvati, is revered by the general public and known by a variety of names, including Sumukha, Ekadanta, Kapila, Gajakarna, Lambodara, Vikath, Vidhnanashaka, Vinayaka, Bhalchandra, and Gajanana. Lord Ganesha's paintings appear incredibly alluring and captivating."
                            },
                            "media":media_urn,
                            "title": {
                                "text": "Lord Ganesha Painting"
                            }
                        }
                    ]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "CONTAINER"
            }
        }
        # print(media_urn)
    response = requests.post(SHARE_URL, headers=headers, json=share_data)
    print(response.text)
    if response.status_code == 201:
            print('Successfully posted on LinkedIn.')
    else:
            print('Error posting on LinkedIn:', response.status_code, response.text)




class Video_post_to_linkedin_group(APIView):
    def get(self,request):
        # Retrieve data from the database (e.g., Post model)
        posts = Linkedln.objects.all().values('content','linkedln_person_urn','linkedln_group_urn','thumbnail_url','access_token','video_url')  # Fetch necessary fields
        print(posts)
        
        if posts: 
            key_to_extract1 = 'linkedln_person_urn'
            urn_id = [d[key_to_extract1] for d in posts]
            # print(chat_id)
            key_to_extract1 = 'linkedln_group_urn'
            group_urn_id = [d[key_to_extract1] for d in posts]

            key_to_extract2 = 'access_token'
            access_token = [d[key_to_extract2] for d in posts]
            # print(access_token)
            for post in posts:
                # Customize the message content here using the retrieved data
                 msg=post['content']
                 thumbnail_url=post['thumbnail_url']
                 http_url=post['video_url']
                 response = requests.head(http_url,allow_redirects=True)
                 video_url = response.url
           
                # Post on each Facebook page
                 for i in range(len(urn_id)):
                    response = post_to_telegram(urn_id[i],group_urn_id[i],access_token[i],msg,video_url,thumbnail_url)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Linkedin."})

# Function to post to Facebook using the Facebook Graph API
def post_to_telegram(urn_id,group_urn_id,access_token,msg,video_url,thumbnail_url):
    import requests
    MEDIA_UPLOAD_URL = 'https://api.linkedin.com/v2/assets?action=registerUpload'
    headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
    media_data = {
            'registerUploadRequest': {
                'recipes': ['urn:li:digitalmediaRecipe:feedshare-video'],
                'owner': f'urn:li:person:{urn_id}',
                'serviceRelationships': [
                    {
                        'relationshipType': 'OWNER',
                        'identifier': 'urn:li:userGeneratedContent'
                    }
                ]
            }
        }

    response1 = requests.post(MEDIA_UPLOAD_URL,headers=headers,json=media_data)
    #    print(response1.status_code)
    #    print("******************************************************")
    result=json.loads(response1.text)
    #    print(result)
    uploadUrl=response1.json()['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
        # ********************************************************************************************
    headers1 = {
            'Authorization': f'Bearer {access_token}',
            "media-type-family": "VIDEO"
        }

    #    with open(video_url, 'rb') as f:
    #         data = f.read()

    response = requests.post(uploadUrl,headers=headers1,data=video_url)
    print(response.status_code)
    print(response.text)
        # ********************************************************************************************

    if response1.status_code == 200:
        media_urn= response1.json()['value']['asset']
            # print(media_urn)
    else:
        print('Error uploading media:', response.status_code, response.text)


        # **************************************************************************************************

    SHARE_URL = 'https://api.linkedin.com/v2/ugcPosts'

    share_data = {
            "author": f"urn:li:person:{urn_id}",
            'containerEntity':f'urn:li:group:{group_urn_id}',
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": "Feeling inspired after meeting so many talented individuals at this year's conference. #talentconnect"
                    },
                    "shareMediaCategory": "VIDEO",
                    "media": [
                        {
                            "status": "READY",
                            "description": {
                                "text":msg
                            },
                            "media":media_urn,
                            "title": {
                                "text": "LinkedIn Talent Connect 2023"
                            },
                            "thumbnails":[{
                                "url":thumbnail_url
                            }]
                        }
                    ]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "CONTAINER"
            }
        }

    response = requests.post(SHARE_URL, headers=headers, json=share_data)
    print(response.text)
    if response.status_code == 201:
            print('Successfully posted on LinkedIn.')
    else:
            print('Error posting on LinkedIn:', response.status_code, response.text)



class Text_post_to_twiter(APIView):
    def get(self, request):
        # Retrieve data from the database (e.g., Post model)
        posts = Twiter.objects.all().values('content','consumer_key','consumer_secret','access_token','access_token_secret')  # Fetch necessary fields
        print(posts)
        if posts: 
            key_to_extract1 = 'consumer_key'
            consumer_key = [d[key_to_extract1] for d in posts]
            key_to_extract2 = 'consumer_secret'
            consumer_secret = [d[key_to_extract2] for d in posts]
            key_to_extract3 = 'access_token'
            access_token = [d[key_to_extract3] for d in posts]
            key_to_extract4 = 'access_token_secret'
            access_token_secret = [d[key_to_extract4] for d in posts]
            for post in posts:
                # Customize the message content here using the retrieved data
                message = post['content']
           
                # Post on each Facebook page
                for i in range(len(consumer_key)):
                    response = post_to_twiter(consumer_key[i], consumer_secret[i], access_token[i],access_token_secret[i],message)
                    print(response)  # Print the response from the Facebook API

        return Response({"message": "Data fetched from the database and posted on Twiter"})

# Function to post to Facebook using the Facebook Graph API
def post_to_twiter(consumer_key,consumer_secret,access_token,access_token_secret,message):
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)

        client = tweepy.Client(
          consumer_key=consumer_key, consumer_secret=consumer_secret,
          access_token=access_token, access_token_secret=access_token_secret
       )
   
        if len(message)<=280:
            client.create_tweet(text=message)
            print("Message Tweeted Successfully")
        else:
            print("Tweet is too long.Please shorten your message.")



# *******************************************************************************************#
# *******************************************************************************************#


# class FacebookPage(APIView):
#     def get(self, request):
#         # Retrieve data from the database (e.g., Post model)
#         posts = BusinessConnect.objects.all().values('content','fb_page_id','fb_page_access_token')  # Fetch necessary fields
#         print(posts)
        
#         if posts: 
#             key_to_extract1 = 'fb_page_id'
#             page_ids = [d[key_to_extract1] for d in posts]
#             key_to_extract2 = 'fb_page_access_token'
#             access_tokens = [d[key_to_extract2] for d in posts]
#             for post in posts:
#                 # Customize the message content here using the retrieved data
#                 message = f"Content: {post['content']}"
#                #  page_ids = post['fb_page_id']
               
#                #  access_tokens = str(post['fb_page_access_token'])
           
#                 # Post on each Facebook page
#                 for i in range(len(page_ids)):
#                     response = post_to_facebook(page_ids[i], access_tokens[i], message)
#                     print(response)  # Print the response from the Facebook API

#         return Response({"message": "Data fetched from the database and posted on Facebook."})

# # Function to post to Facebook using the Facebook Graph API
# def post_to_facebook(page_id, access_token, message):
#     import requests
    
#     url = f"https://graph.facebook.com/{page_id}/feed"
#     params = {
#         'message': message,
#         'access_token': access_token
#     }
    
#     response = requests.post(url,params=params)
#     return response.json()  # Returns the response from the Facebook API



# **************************************88*********************************************
# *************************************************************************************

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Use this decorator if CSRF protection is enabled and it's not a concern for your endpoint
def FacebookPage(request):
    if request.method == 'POST':
        try:
            posts = json.loads(request.body)
            print(posts)
            message=posts['text']
            print(message)
            link_url=posts['link']
            data=posts['data']
            
            if data: 
               key_to_extract1='label'
               page_ids = [d[key_to_extract1] for d in data]
               print(page_ids)
               key_to_extract2 = 'value'
               access_tokens = [d[key_to_extract2] for d in data]
               print(access_tokens)
         
            for i in range(len(page_ids)):
               response = post_to_facebook(page_ids[i],access_tokens[i],message,link_url)
               print(response)  # Print the response from the Facebook API
            
            # Return a response if needed
            return JsonResponse({'message': 'Data received successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
 # Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id,access_token,message,link_url):
    import requests
    upload_url = f"https://graph.facebook.com/v18.0/{page_id}/feed"
    params = {
        'message': message,
        'access_token': access_token,
        'link':link_url,
    }
    
    response = requests.post(upload_url,params=params)
    return response.json()  # Returns the response from the Facebook API


# *************************************New For Image*********************************************
# *************************************************************************************

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Use this decorator if CSRF protection is enabled and it's not a concern for your endpoint
def FacebookPage(request):
    # if request.method == 'POST':
    if request.method == 'POST' and request.FILES:
        try:
            image_url=request.FILES['file']
            posts=json.loads(request.body)
            print(posts)
            message=posts['text']
            # print(message)
            # image_url="https://i.ytimg.com/an_webp/8tEVEi4Zq38/mqdefault_6s.webp?du=3000&sqp=CLStxasG&rs=AOn4CLAgmAgJd5hTTtZl4jQId4T51s9QUg"
            data=posts['data']  
            if data: 
               key_to_extract1='label'
               page_ids = [d[key_to_extract1] for d in data]
            #    print(page_ids)
               key_to_extract2 = 'value'
               access_tokens = [d[key_to_extract2] for d in data]
            #    print(access_tokens)
            # for post in data:
                # Customize the message content here using the retrieved data
                # message = post['text']
                # print(message)
                # image_url = post['file']
                # print(image_url)
                # page_ids = post['fb_page_id']
               
                # access_tokens = str(post['fb_page_access_token'])
           
                # Post on each Facebook page
            # print(len(page_ids))
            # for i in range(len(page_ids)):
            # with open('d:\Global Project\connectifyindia\public\images\8 Legal Aspire Blog.png','rb') as file:
            #     image_url=file.read()
                # print(image_url)
            for i in range(len(page_ids)):
               response = post_to_facebook(page_ids[i],access_tokens[i],message,image_url)
               print(response)  # Print the response from the Facebook API
            
            # Return a response if needed
            return JsonResponse({'message': 'Data received successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
 # Function to post to Facebook using the Facebook Graph API
def post_to_facebook(page_id,access_token,message,image_url):
    import requests
    upload_url = f"https://graph.facebook.com/v17.0/{page_id}/photos"
    # with open("d:\Global Project\connectifyindia\public\images\8 Legal Aspire Blog.png",'rb') as file:
    # image_url=file.read()
    params = {
          'message': message,
          'access_token': access_token,
          'url':image_url,
    }
    response = requests.post(upload_url,params=params)
    return response.json()  # Returns the response from the Facebook API


# ******************************** New for File *****************************************

# views.py
from rest_framework.views import APIView
# from rest_framework.response import Response
from django.conf import settings
import os
from urllib.parse import unquote
# from rest_framework.parsers import MultiPartParser,FormParser
# from .serializer import FileUploadSerializer

# import json
class FileUploadView(APIView):
    def post(self,request):
        file_obj = request.FILES.get('upload')
        # print(file_obj.name)
        textData = request.POST.get('description')
        print(textData)
        link_url = request.POST.get('Link')
        print(link_url)
        selectedData = request.POST.get('selectedOption')
        dicData=json.loads(selectedData)

        # media_path = os.path.join(settings.MEDIA_ROOT,str(file_obj.name))  
        # print(media_path)

# **********************************************************************************
        
        # print("Json data come here........")
        # data=requests.get("https://jsonplaceholder.typicode.com/photos")
        # result=data.text
        # jsondata=json.loads(result)
        # image=jsondata[1]['url']
        # print(jsondata[0]['url'])

# ******************************************************************************
        # print("Connectify India server data come here........")
        # data=requests.get("https://connectifyglobalbackend.azurewebsites.net/connectifyindia/videolist")
        # result=data.text
        # # print(result)
        # final_result=json.loads(result)
        # dic=final_result['results']
        # image=dic[0]['image_url']
        # video=dic[0]['video']
        # print(image)
#***************************************************************************** 
        # print(final_result)
        # jsondata=json.loads(final_result)
        # image=final_result['image_url']
        # print(image)
        # print(final_result)


        
        # ************************************************************************#
        # with open(settings.MEDIA_ROOT + str(file_obj), 'wb+') as destination:
        #     for chunk in file_obj.chunks():
        #         destination.write(chunk)
        # print(destination)
# *********************************************************************************
        # with open(media_path, 'wb+') as destination:
        #  for chunk in file_obj.chunks():
        #     destination.write(chunk)
        #     # print(destination)
        # absolute_url = request.build_absolute_uri(settings.MEDIA_URL+str(file_obj.name))

# ************************************************************************************

        # absolute_url=unquote(absolute_url)
        # print(absolute_url)

        # print(type(absolute_url))
        # absolute_url=f"http://connectifyglobalbackend.azurewebsites.net/media/Connectify_India_company_profile.png"
        
        # print(absolute_url)
        # file_url=absolute_url.replace("http://", "https://")
        # print(absolute_url)

        # print(dumpdata[0]['fb_page_access_token'])
        # print("*********************************************")
        # print(selectedData[0]['value'])
            
# ****************************************************************************************
            
        key_to_extract1='value'
        page_ids=[d[key_to_extract1] for d in dicData]
        print(page_ids)

        key_to_extract2='fb_page_access_token'
        access_tokens=[d[key_to_extract2] for d in dicData]
        print(access_tokens)

        key_to_extract3='label'
        fb_page_names = [d[key_to_extract3] for d in dicData]
        print(fb_page_names)


# ****************************************************************************************#

          # Determine the file type (e.g., image, video, document)
        file_type = get_file_type(self,link_url)
        # Perform actions based on the file type
        if file_type == 'image':
            # Post image to Facebook using Graph API
            for i in range(len(page_ids)):
               response = image_post_to_facebook_page(page_ids[i],access_tokens[i],textData,link_url)
               print(response)  # Print the response from the Facebook AP
               print(link_url)

            return Response({'Message':'Video and Text processed successfully and posted on page which are selected on the dropdown',
                  'Image_url':link_url,
                  'Response':response
                  })


        elif file_type == 'video':
            # Post video to Facebook using Graph API
            for i in range(len(page_ids)):
               response = video_post_to_facebook_page(page_ids[i],access_tokens[i],textData,link_url)
               print(response)  # Print the response from the Facebook AP
            #    print(absolute_url)
            return Response({'Message':'Video and Text processed successfully and posted on page which are selected on the dropdown',
                  'Video_url':link_url,
                  'Response':response
                  })
        

        # elif file_type == 'document':
        #     # Post document to Facebook using Graph API

        # else:
            # Handle other file types

        # if link_url:
        #     for i in range(len(page_ids)):
        #        response = Link_post_to_facebook_page(page_ids[i],access_tokens[i],textData,link_url)
        #        print(response)  # Print the response from the Facebook AP
        #     return Response({'message':'Link and Text processed successfully and posted on page which are selected on the dropdown'})
    

        # # return Response({'message': 'File uploaded and posted to Facebook'})



        # ****************************************************************************************#

 # Function to post to Facebook using the Facebook Graph API

#  for image
def image_post_to_facebook_page(page_id,access_token,textData,absolute_url):
    import requests
    # absolute_url="http://connectifyglobalbackend.azurewebsites.net/media/8%20Legal%20Aspire%20Blog.png"

    upload_url= f"https://graph.facebook.com/v18.0/{page_id}/photos"
    params ={
          'message':textData,
          'access_token':access_token
        #   'url':absolute_url,
    }
    files={
        'url':absolute_url
    },
    response=requests.post(upload_url,params=params,files=files)
    return response.json()  # Returns the response from the Facebook API
    

# for video
def video_post_to_facebook_page(page_id,access_token,textData,absolute_url):
    # print(absolute_url)
    import requests
    # absolute_url=f"http://connectifyglobalbackend.azurewebsites.net/media/Connectify_India_Company_Profile.mp4"
    video_response = requests.post(f'https://graph-video.facebook.com/v18.0/{page_id}/videos',
              files={
                   'file_url':absolute_url
                   },
#                #  files={'source': open('d:\Global Project\connectifyindia\public\media\short_video1.mp4', 'rb')},

         params={
            'access_token':access_token,
            'description':textData
            # 'file_url':absolute_url
            }
            )
    
    return video_response.json()
 
# for Link with text
# def Link_post_to_facebook_page(page_id,access_token,textData,link_url):
#     import requests
#     upload_url = f"https://graph.facebook.com/v18.0/{page_id}/feed"
#     params = {
#         'message':textData,
#         'access_token':access_token,
#         'link':link_url,
#     }
    
#     response=requests.post(upload_url,params=params)
#     return response.json() 

# ****************************************************************************************#

# get file type and return
def get_file_type(self,link_url):
        # Implement logic to classify file types based on file name or content
        # Example logic to classify based on file extension
        if str(link_url).lower().endswith(('.png', '.jpg', '.jpeg', '.gif','.webp')):
            return 'image'
        elif str(link_url).lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            return 'video'
        # elif file_name.lower().endswith(('.doc', '.docx', '.pdf', '.txt')):
        #     return 'document'
        # else:
        #     return 'other'


# *****************************************************************************************************
# from .models import FileUpload
from rest_framework.response import Response
# from rest_framework import generics
class FileUploadViewWithSerialize(APIView):
        # parser_classes = [MultiPartParser]
        def post(self, request, format=None):
        #  serializer = FileUploadSerializer(data=request.data)
        #  if serializer.is_valid():
            file_obj = request.FILES.get('upload')
            print(file_obj.name)
            textData = request.POST.get('description')
            print(textData)
            link_url = request.POST.get('Link')
            print(link_url)
            selectedData = request.POST.get('selectedOption')
            dicData=json.loads(selectedData)

            # first_elements = [t[0] for t in auth_data]  # List comprehension
            # print(first_elements)

            # for item in auth_data:
            #     name = item['name']
            #     # print(name)
            #     access_token = item['access_token']
            #     # print(access_token)
            #     page_id=item['page_id']
            #     # print(page_id)
            #     label=item['label']
            #     # print(label)

            key_to_extract1='value'
            page_ids=[d[key_to_extract1] for d in dicData]
            print(page_ids)

            key_to_extract2='fb_page_access_token'
            access_tokens=[d[key_to_extract2] for d in dicData]
            print(access_tokens)

            key_to_extract3='label'
            fb_page_names = [d[key_to_extract3] for d in dicData]
            print(fb_page_names)




            # Process the uploaded file (save, manipulate, etc.)
            # Example: Save the file to a specific directory
            with open(f'media/{file_obj.name}', 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)

            absolute_url = request.build_absolute_uri(settings.MEDIA_URL+str(file_obj))
            # print(absolute_url)
            
            # return Response({'message': 'File uploaded successfully'})
        #  else:
        #     return Response(serializer.errors, status=400)
         


        #     textData1 = serializer.validated_data['content']
        #     print(textData1)
        #     file_obj1 = serializer.validated_data['file']
        #     print(file_obj1)
        #     all_auth_data = serializer.validated_data['auth_data']
        #     print(all_auth_data)

        # file_obj = request.FILES.get('upload')
        # print(file_obj.name)
        # textData = request.POST.get('description')
        # print(textData)
        # link_url = request.POST.get('Link')
        # print(link_url)
        # selectedData = request.POST.get('selectedOption')
        # dicData=json.loads(selectedData)
        # media_path = os.path.join(settings.MEDIA_ROOT,str(file_obj.name))  
        # print(media_path)

        # with open(media_path,'r') as file:
        #     absolute_url=file.read()
        # print("absolute url:",absolute_url)

# **********************************************************************************
        
        # print("Json data come here........")
        # data=requests.get("https://jsonplaceholder.typicode.com/photos")
        # result=data.text
        # jsondata=json.loads(result)
        # image=jsondata[1]['url']
        # print(jsondata[0]['url'])

# ******************************************************************************
        # print("Connectify India server data come here........")
        # data=requests.get("https://connectifyglobalbackend.azurewebsites.net/connectifyindia/videolist")
        # result=data.text
        # # print(result)
        # final_result=json.loads(result)
        # dic=final_result['results']
        # image=dic[0]['image_url']
        # video=dic[0]['video']
        # print(image)
#***************************************************************************** 
        # print(final_result)
        # jsondata=json.loads(final_result)
        # image=final_result['image_url']
        # print(image)
        # print(final_result)


        
        # ************************************************************************#
        # with open(settings.MEDIA_ROOT + str(file_obj), 'wb+') as destination:
        #     for chunk in file_obj.chunks():
        #         destination.write(chunk)
        # print(destination)
# *********************************************************************************
        # with open(media_path, 'wb+') as destination:
        #  for chunk in file_obj.chunks():
        #     destination.write(chunk)
        #     # print(destination)
        # absolute_url = request.build_absolute_uri(settings.MEDIA_URL+str(file_obj.name))

# ************************************************************************************         
        # key_to_extract1='value'
        # page_ids=[d[key_to_extract1] for d in dicData]
        # print(page_ids)

        # key_to_extract2='fb_page_access_token'
        # access_tokens=[d[key_to_extract2] for d in dicData]
        # print(access_tokens)

        # key_to_extract3='label'
        # fb_page_names = [d[key_to_extract3] for d in dicData]
        # print(fb_page_names)


# ****************************************************************************************#

          # Determine the file type (e.g., image, video, document)
            file_type = get_file_type(self,file_obj)
        # Perform actions based on the file type
            if file_type == 'image':
            # Post image to Facebook using Graph API
             for i in range(len(page_ids)):
               response = image_post_to_facebook_page(page_ids[i],access_tokens[i],textData,absolute_url)
               print(response)  # Print the response from the Facebook AP
            #    print(absolute_url)

             return Response(
                 {'message':'Image and Text processed successfully and posted on page which are selected on the dropdown',
                  'image_url':absolute_url,
                  'response':response
                  })


            elif file_type == 'video':
            # Post video to Facebook using Graph API
             for i in range(len(page_ids)):
               response = video_post_to_facebook_page(page_ids[i],access_tokens[i],textData,absolute_url)
               print(response)  # Print the response from the Facebook AP
            #    print(absolute_url)
             return Response(
                 {'message':'Video and Text processed successfully and posted on page which are selected on the dropdown',
                  'video_url':absolute_url,
                  'response':response
                  })
        


        # ****************************************************************************************#

 # Function to post to Facebook using the Facebook Graph API

#  for image
def image_post_to_facebook_page(page_id,access_token,textData,absolute_url):
    print(absolute_url)
    import requests
    upload_url= f"https://graph.facebook.com/v18.0/{page_id}/photos"
    params ={
          'message':textData,
          'access_token':access_token,
          'url':absolute_url,
    }
    files={
                   'url':absolute_url
                   },
    response=requests.post(upload_url,params=params)
    return response.json()  # Returns the response from the Facebook API
    

# for video
def video_post_to_facebook_page(page_id,access_token,textData,absolute_url):
    print(absolute_url)
    import requests
    # absolute_url=f"http://connectifyglobalbackend.azurewebsites.net/media/Connectify_India_Company_Profile.mp4"
    video_response = requests.post(f'https://graph-video.facebook.com/v18.0/{page_id}/videos',
            #   files={
            #        'file_url':absolute_url
            #        },
#                #  files={'source': open('d:\Global Project\connectifyindia\public\media\short_video1.mp4', 'rb')},

         params={
            'access_token':access_token,
            'description':textData,
            'file_url':absolute_url
            }
            )
    
    return video_response.json()
 
# ****************************************************************************************#

# get file type and return
def get_file_type(self,file_obj):
        # Implement logic to classify file types based on file name or content
        # Example logic to classify based on file extension
        if str(file_obj).lower().endswith(('.png', '.jpg', '.jpeg', '.gif','.webp')):
            return 'image'
        elif str(file_obj).lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            return 'video'
       


