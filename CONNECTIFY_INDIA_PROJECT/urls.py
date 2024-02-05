"""CONNECTIFY_INDIA_PROJECT URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:path('', Home.as_view(),name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from connectifyindia import views
from django.conf.urls.static import static
from django.conf import settings
from CONNECTIFY_INDIA_PROJECT import deployment


urlpatterns=[
    path('auth/',include('drf_social_oauth2.urls', namespace='drf')),
    path('api/user/', include('users.urls', namespace='users')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('admin/',admin.site.urls),
    path('ainaw/',include('Ainaw_And_Social_Connect.urls')),
    path('simply-counsel/',include('Counsel_For_Academic_And_Job.urls')),
    path('legal-aspire/',include('Legal_And_Counsel.urls')),
    path('business-connect/',include('Project_Youth_And_Business_Enterpreneur_Network.urls')),
    path('connectifyindia/',include('ConnectifyIndia.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('social-media/api/',include('SocialMediaApp.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(deployment.STATIC_URL, document_root=deployment.STATIC_ROOT)
    urlpatterns += static(deployment.MEDIA_URL, document_root=deployment.MEDIA_ROOT)


