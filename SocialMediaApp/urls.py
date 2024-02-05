from django.urls import path
from SocialMediaApp import views

urlpatterns = [
    path('connectifyindia/',views.ConnectifyIndiaListCreateApiView.as_view(),name='connectifyindia'),
    path('connectifyindia/detail/<int:pk>/',views.ConnectifyIndiaRetrieveUpdateDestroyApiView.as_view(),name='connectifyindia-detail'),

    # ************************(((Facebook)))****************************************

    path('facebook/',views.FacebookListCreateApiView.as_view(),name='facebook'),
    path('facebook/<int:pk>/',views.FacebookRetrieveUpdateDestroyApiView.as_view(),name='facebook-details'),
    path('upload/', views.FileUploadView.as_view(), name='file-upload'),
    path('serialize-upload/', views.FileUploadViewWithSerialize.as_view(), name='serialize-upload'),

    # ******************************************************************************

    path('simplycounsel/',views.SimplyCounselListCreateApiView.as_view(),name='simplycounsel'),
    path('simplycounsel/detail/<int:pk>/',views.SimplyCounselRetrieveUpdateDestroyApiView.as_view(),name='simplycounsel-detail'),

    path('legalaspire/',views.LegalAspireListCreateApiView.as_view(),name='legalaspire'),
    path('legalaspire/detail/<int:pk>/',views.LegalAspireRetrieveUpdateDestroyApiView.as_view(),name='legalaspire-detail'),

    path('ainaw/',views.AinawListCreateApiView.as_view(),name='ainaw'),
    path('ainaw/detail/<int:pk>/',views.AinawRetrieveUpdateDestroyApiView.as_view(),name='ainaw-detail'),

    path('businessconnect/',views.BusinessConnectListCreateApiView.as_view(),name='businessconnect'),
    path('businessconnect/detail/<int:pk>/',views.BusinessConnectRetrieveUpdateDestroyApiView.as_view(),name='businessconnect-detail'),

    path('instagram/',views.InstagramListCreateApiView.as_view(),name='instagram'),
    path('instagram/detail/<int:pk>/',views.InstagramRetrieveUpdateDestroyApiView.as_view(),name='instagram-detail'),
    
    path('Twiter/',views.TwiterListCreateApiView.as_view(),name='twiter'),
    path('Twiter/detail/<int:pk>/',views.TwiterRetrieveUpdateDestroyApiView.as_view(),name='twiter-detail'),

    path('Linkedln/',views.LinkedlnListCreateApiView.as_view(),name='Linkedln'),
    path('Linkedln/detail/<int:pk>/',views.LinkedlnRetrieveUpdateDestroyApiView.as_view(),name='Linkedln-detail'),

    path('whatsapps/',views.WhatsappListCreateApiView.as_view(),name='whatsapp'),
    path('whatsapp/<int:pk>/',views.WhatsappRetrieveUpdateDestroyApiView.as_view(),name='whatsapp-detail'),

    path('telegrams/',views.TelegramListCreateApiView.as_view(),name='telegram'),
    path('telegram/<int:pk>/',views.TelegramRetrieveUpdateDestroyApiView.as_view(),name='telegram-detail'),

# ******************************CONNECTIFY INDIA******************************

    path('connectifyindia-page/text/',views.Text_post_to_connectifyindia_page.as_view(),name='connectifyindia-page-text'),
    path('connectifyindia-page/image/',views.Image_post_to_connectifyindia_page.as_view(),name='connectifyindia-page-image'),
    path('connectifyindia-page/video/',views.Video_post_to_connectifyindia_page.as_view(),name='connectifyindia-page-video'),
    path('connectifyindia-page/link/',views.Link_post_to_connectifyindia_page.as_view(),name='connectifyindia-page-link'),

# ******************************SIMPLY COUNSEL******************************

    path('simplycounsel-page/image/',views.Image_post_to_simplycounsel_page.as_view(),name='simplycounsel-page-image'),
    path('simplycounsel-page/video/',views.Video_post_to_simplycounsel_page.as_view(),name='simplycounsel-page-video'),
    path('simplycounsel-page/link/',views.Link_post_to_simplycounsel_page.as_view(),name='simplycounsel-page-link'),
    path('simplycounsel-page/text/',views.Text_post_to_simplycounsel_page.as_view(),name='simplycounsel-page-text'),

    # ******************************LEGAL ASPIRE******************************

    path('legalaspire-page/text/',views.Text_post_to_legalaspire_page.as_view(),name='legalaspire-page-text'),
    path('legalaspire-page/image/',views.Image_post_to_legalaspire_page.as_view(),name='legalaspire-page-image'),
    path('legalaspire-page/video/',views.Video_post_to_legalaspire_page.as_view(),name='legalaspire-page-video'),
    path('legalaspire-page/link/',views.Link_post_to_legalaspire_page.as_view(),name='legalaspire-page-link'),

# ******************************AINAW******************************

    path('ainaw-page/image/',views.Image_post_to_ainaw_page.as_view(),name='ainaw-page-image'),
    path('ainaw-page/video/',views.Video_post_to_ainaw_page.as_view(),name='ainaw-page-video'),
    path('ainaw-page/link/',views.Link_post_to_ainaw_page.as_view(),name='ainaw-page-link'),
    path('ainaw-page/text/',views.Text_post_to_ainaw_page.as_view(),name='ainaw-page-text'),


# ******************************BUSINESS CONNECT******************************

    path('businessconnect-page/image/',views.Image_post_to_businessconnect_page.as_view(),name='businessconnect-page-image'),
    path('businessconnect-page/video/',views.Video_post_to_businessconnect_page.as_view(),name='businessconnect-page-video'),
    path('businessconnect-page/link/',views.Link_post_to_businessconnect_page.as_view(),name='businessconnect-page-link'),
    path('businessconnect-page/text/',views.Text_post_to_businessconnect_page.as_view(),name='businessconnect-page-text'),

    
# ******************************INSTAGRAM******************************


    path('instagram/image/',views.Image_post_to_instagram.as_view(),name='instagram-image'),
    path('instagram/video/',views.Video_post_to_instagram.as_view(),name='instagram-video'),


# ******************************WHATSAPP******************************

    path('whatsapp/text/',views.Text_post_to_whatsapp.as_view(),name='whatsapp-text'),
    path('whatsapp/image/',views.Image_post_to_whatsapp.as_view(),name='whatsapp-image'),
    path('whatsapp/video/',views.Video_post_to_whatsapp.as_view(),name='whatsapp-video'),
    path('whatsapp/location/',views.Location_post_to_whatsapp.as_view(),name='whatsapp-location'),
    # path('whatsapp/document/',views.Document_post_to_whatsapp.as_view(),name='whatsapp-document'),


# ******************************TELEGRAM******************************

    path('telegram/text/',views.Text_post_to_telegram.as_view(),name='telegram-text'),
    path('telegram/image/',views.Image_post_to_telegram.as_view(),name='telegram-image'),
    path('telegram/video/',views.Video_post_to_telegram.as_view(),name='telegram-video'),
    path('telegram/document/',views.Document_post_to_telegram.as_view(),name='telegram-document'),

# ******************************LINKEDIN******************************

    path('linkedin/article/',views.Article_post_to_linkedin.as_view(),name='linkedin-article'),
    path('linkedin/image/',views.Image_post_to_linkedin.as_view(),name='linkedin-image'),
    path('linkedin/video/',views.Video_post_to_linkedin.as_view(),name='linkedin-video'),
    # Linkedin Group
    path('linkedin-group/article/',views.Article_post_to_linkedin_group.as_view(),name='linkedin-group-article'),
    path('linkedin-group/image/',views.Image_post_to_linkedin_group.as_view(),name='linkedin-group-image'),
    path('linkedin-group/video/',views.Video_post_to_linkedin_group.as_view(),name='linkedin-group-video'),
    # path('linkedin/document/',views.Document_post_to_linkedin.as_view(),name='linkedin-document'),

    # *************************TWITER*******************************************
    path('twiter/text/',views.Text_post_to_twiter.as_view(),name='twiter-text'),
    # path('twiter/image/',views.Image_post_to_twiter.as_view(),name='twiter-image'),
    # path('twiter/video/',views.Video_post_to_twiter.as_view(),name='twiter-video'),
    path('facebookpage/',views.FacebookPage,name='facebookpage'),

]




