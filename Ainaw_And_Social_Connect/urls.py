from django.urls import path
from Ainaw_And_Social_Connect import views


urlpatterns = [
    path('register-ngo/',views. RegisterNGOCreateView.as_view()),
    path('non-register-ngo/',views.NonRegisterNGOCreateView.as_view()),
    path('social-activist/',views.SocialActivistCreateView.as_view()),
    path('business/',views.BusinessCreateView.as_view()),
    path('admin/',views.AdminCreateView.as_view()),
    path('reg-ngo-login/',views.RegisterNGO_login_view),
    path('admin-login/',views. Admin_login_view),
    path('non-reg-ngo-login/',views.NonRegisterNGO_login_view),
    path('social-activist-login/',views.SocialActivist_Enterpreneur_login_view),
    path('business-login/',views.Business_Manpower_login_view),

]