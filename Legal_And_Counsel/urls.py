from django.urls import path
from Legal_And_Counsel import views


urlpatterns = [
    path('student_intern/',views.Student_InternCreateView.as_view()),
    path('advocate/',views.Advocate_LawyerCreateView.as_view()),
    path('consumer/',views.Consumer_UserCreateView.as_view()),
    path('content-publisher/',views.Content_ManagerCreateView.as_view()),
    path('legal-admin/',views.AdminCreateView.as_view()),
    path('student-login/',views.Student_login_view),
    path('admin-login/',views.Admin_login_view),
    path('consumer-login/',views.Consumer_login_view),
    path('content-publisher-login/',views.ContentPublisher_login_view),
    path('advocate-login/',views.Advocate_login_view),

    

]