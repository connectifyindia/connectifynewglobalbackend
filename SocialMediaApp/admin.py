from django.contrib import admin
from .models import ConnectifyIndia,SimplyCounsel,LegalAspire,Ainaw,BusinessConnect,Instagram,Twiter,Linkedln,Telegram,Whatsapp,FacebookModel


# Register your models here.
class ConnectifyIndiaAdmin(admin.ModelAdmin):
   list_display=['id','image_url','video_url','content','fb_page_id','fb_page_access_token']
admin.site.register(ConnectifyIndia,ConnectifyIndiaAdmin)

# ***********************Facebook****************************
class FacebookAdmin(admin.ModelAdmin):
   list_display=['id','fb_page_id','fb_page_access_token','fb_group_id','fb_user_access_token','fb_page_name','fb_group_name','logo']
admin.site.register(FacebookModel,FacebookAdmin)

# ***********************************************************

class SimplyCounselAdmin(admin.ModelAdmin):
   list_display=['id','image_url','video_url','content','fb_page_id','fb_page_access_token']
admin.site.register(SimplyCounsel,SimplyCounselAdmin)

class LegalAspireAdmin(admin.ModelAdmin):
   list_display=['id','image_url','video_url','content','fb_page_id','fb_page_access_token']
admin.site.register(LegalAspire,LegalAspireAdmin)

class AinawAdmin(admin.ModelAdmin):
   list_display=['id','image_url','video_url','content','fb_page_id','fb_page_access_token']
admin.site.register(Ainaw,AinawAdmin)

class BusinessConnectAdmin(admin.ModelAdmin):
   list_display=['id','image_url','video_url','content','fb_page_id','fb_page_access_token']
admin.site.register(BusinessConnect,BusinessConnectAdmin)

class InstagramAdmin(admin.ModelAdmin):
   list_display=['id','image_url','video_url','content','fb_page_id','fb_page_access_token','instagram_user_id']
admin.site.register(Instagram,InstagramAdmin)

class TwiterAdmin(admin.ModelAdmin):
   list_display=['id','image_url','video_url','content','bearer_token','consumer_key','consumer_secret','access_token','access_token_secret']
admin.site.register(Twiter,TwiterAdmin)

class LinkedlnAdmin(admin.ModelAdmin):
   list_display=['id','image_url','video_url','content','access_token','linkedln_person_urn','linkedln_group_urn']
admin.site.register(Linkedln,LinkedlnAdmin)

class TelegramAdmin(admin.ModelAdmin):
   list_display=['id','image_url','video_url','content','chat_id','bot_token','document']
admin.site.register(Telegram,TelegramAdmin)

class WhatsappAdmin(admin.ModelAdmin):
   list_display=['id','image_url','video_url','content','recepient_number','city_name']
admin.site.register(Whatsapp,WhatsappAdmin)






