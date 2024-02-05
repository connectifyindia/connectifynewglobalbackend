from django.db import models
# Create your models here.
class common(models.Model):  # COMM0N For All Model
    image_url=models.ImageField(null=True,blank=True)
    video_url=models.FileField(null=True,blank=True)
    content=models.TextField(null=True,blank=True)
    link_url=models.URLField(null=True,blank=True)
    document=models.FileField(null=True,blank=True)

    class Meta: 
        abstract = True
class Facebook(models.Model):  # FACEBOOK 
    fb_page_id=models.CharField(max_length=30,null=True,blank=True)
    fb_page_access_token=models.CharField(max_length=500,null=True,blank=True)
    fb_group_id=models.CharField(max_length=30,null=True,blank=True)
    fb_user_access_token=models.CharField(max_length=500,null=True,blank=True)

    class Meta:
        abstract=True

class ConnectifyIndia(common,Facebook):
    pass
class SimplyCounsel(common,Facebook):
    pass
class LegalAspire(common,Facebook):
    pass
class Ainaw(common,Facebook):
    pass
class BusinessConnect(common,Facebook):
    pass
class Instagram(common,Facebook):  # Instagram  
    instagram_user_id = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.instagram_user_id
    
class Twiter(common):  # Instagram  
    bearer_token=models.CharField(max_length=500,null=True,blank=True)
    consumer_key=models.CharField(max_length=100,null=True,blank=True)
    consumer_secret=models.CharField(max_length=200,null=True,blank=True)
    access_token=models.CharField(max_length=500,null=True,blank=True)
    access_token_secret=models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.consumer_key

class Linkedln(common): #Linkedln
    access_token=models.CharField(max_length=500,null=True,blank=True)
    linkedln_person_urn=models.CharField(max_length=100,null=True,blank=True)
    linkedln_group_urn=models.CharField(max_length=20,null=True,blank=True)
    thumbnail_url=models.ImageField(null=True,blank=True)

class Telegram(common):
    chat_id=models.CharField(max_length=100,null=True,blank=True)
    bot_token=models.CharField(max_length=500,null=True,blank=True)
    document=models.FileField(null=True,blank=True)

    def __str__(self):
        return self.chat_id

class Whatsapp(common):
    recepient_number=models.CharField(max_length=15,null=True,blank=True)
    phone_number_id=models.CharField(max_length=100,null=True,blank=True)
    WhatsApp_Business_Account_ID=models.CharField(max_length=100,null=True,blank=True)
    auth_token=models.CharField(max_length=500)
    city_name=models.CharField(max_length=100,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    longitude=models.CharField(max_length=100,null=True,blank=True)
    latitude=models.CharField(max_length=100,null=True,blank=True)

class FacebookModel(Facebook):
    fb_page_name=models.CharField(max_length=150,null=True,blank=True)
    fb_group_name=models.CharField(max_length=150,null=True,blank=True)
    logo=models.ImageField(null=True,blank=True)

class FileUpload(models.Model):
    # content=models.TextField(null=True,blank=True)
    file=models.ImageField(null=True,blank=True)
    # auth_data=models.Char(null=True,blank=True)




    


