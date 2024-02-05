from django.contrib import admin
from .models import NewUser,UserProfile


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['email','username','first_name']
admin.site.register(NewUser,UserAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['module','category','subcategory']
admin.site.register(UserProfile,UserProfileAdmin)