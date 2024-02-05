from django.urls import path
from ConnectifyIndia import views

urlpatterns = [
    path('publisher/',views.PublisherCreateView.as_view()),
    path('manager/',views.ManagerCreateView.as_view()),
    path('consumer/',views.ConsumerCreateView.as_view()),
    path('businessdeveloper/',views.BusinessDeveloperCreateView.as_view()),
    path('admin/',views.AdminCreateView.as_view()),
    path('publisher-login/',views.Publisher_login_view),
    path('manager-login/',views.Manager_login_view),
    path('consumer-login/',views.Consumer_login_view),
    path('businessdeveloper-login/',views.BusinessDeveloper_login_view),
    path('admin-login/',views.Admin_login_view),
    path('bloglist/',views.BlogListView.as_view(),name='bloglist'),
    path('blogdetail/<slug:slug>/',views.BlogDetailView.as_view(),name='blog-detail'),
    path('doclist/',views.DocListView.as_view(),name="doclist"),
    path('docdetail/<slug:slug>/', views.MyDocDetail.as_view(), name='doc-detail'),
    path('videolist/',views.TestimonialVideoListView.as_view(),name='videolist'),
    path('SuccessStory/',views.SuccessStoryListView.as_view(),name='successstorylist'),
    path('SuccessStoryDetail/<slug:slug>/',views.SuccessStoryDetailView.as_view(),name='success-story-detail'),
    path('document/',views.DocumentListView.as_view(),name='documentlist'),
    path('documentdetail/<slug:slug>/',views.DocumentDetailView.as_view(),name='document-detail'),
    path('carreer/',views.CarreerCreateView.as_view()),
    path('bootcamp-register/',views.BootcampRegistrationView.as_view()),
    path('bootcamp-list/',views.BootcampListView.as_view(),name='bootcamplist'),
    path('bootcamp-detail/<slug:slug>/',views.BootcampDetailView.as_view(),name='bootcamp-detail'),
    path('api/form/', views.FormAPIView.as_view()),
    path('api/form1/', views.FormAPIView1.as_view()),
    path('api/form2/', views.FormAPIView2.as_view()),
    path('api/form3/', views.FormAPIView3.as_view()),
    path('api/form4/', views.FormAPIView4.as_view()),
    path('api/form5/', views.FormAPIView5.as_view()),
    path('api/form6/', views.FormAPIView6.as_view()),
    path('api/form7/', views.FormAPIView7.as_view()),
    path('feedback/', views.FeedBackAPIView.as_view()),


    

]