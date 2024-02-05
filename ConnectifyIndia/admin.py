from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from .models import Blog,Document,Doc,Bootcamp,SuccessStory,VideoTestimonial
class BlogAdmin(admin.ModelAdmin):
    # def display_content(self, instance):
    #     return format_html(instance.content)

    # display_content.short_description = 'Content'

    list_display=['id','slug','image_url','title','date']
admin.site.register(Blog,BlogAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display=['id','slug','title','image_url','category','sub_category','document']
admin.site.register(Document,DocumentAdmin)

class DocAdmin(admin.ModelAdmin):
    # def display_content_doc(self, instance):
    #     return format_html(instance.content)

    # display_content_doc.short_description = 'Content'
    list_display=['id','slug','date','title','image_url','category']
admin.site.register(Doc,DocAdmin)

class BootcampAdmin(admin.ModelAdmin):
    list_display=['id','slug','title','heading1','heading2','bootcamp_date_detail','bootcamp_time_detail','bootcamp_starting_date','image_url1','image_url2','url']
admin.site.register(Bootcamp,BootcampAdmin)

class SuccessStoryAdmin(admin.ModelAdmin):
    # def display_content_success(self, instance):
    #     return format_html(instance.content)
    # display_content_success.short_description = 'Content'
    list_display=['id','slug','title','image_url','date']
admin.site.register(SuccessStory,SuccessStoryAdmin)

class VideoTestimonialAdmin(admin.ModelAdmin):
    list_display=['id','title','name','description','video']
admin.site.register(VideoTestimonial,VideoTestimonialAdmin)

