from django.urls import path
from Project_Youth_And_Business_Enterpreneur_Network import views
urlpatterns = [
    path('organisation/',views.OrganisationCreateView.as_view()),
    path('intern-jobseeker-student/',views.Intern_JobSeekerStudentCreateView.as_view()),
    path('startup/',views.StartupCreateView.as_view()),
    path('consultant/',views.ConsultantCreateView.as_view()),
    path('admin/',views.AdminCreateView.as_view()),
    path('organisation-login/',views.Organisation_login_view),
    path('intern-jobseeker-student-login/',views.Intern_JobSeekerStudent_login_view),
    path('startup-login/',views.Startup_login_view),
    path('consultant-login/',views.Consultant_login_view),
    path('admin-login/',views.Admin_login_view),


]