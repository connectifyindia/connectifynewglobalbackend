from django.urls import path
from Counsel_For_Academic_And_Job import views


urlpatterns = [
    path('student-register/',views.StudentCreateView.as_view()),
    path('trainer/',views.TrainerCreateView.as_view()),
    path('professional/',views.ProfessionalCreateView.as_view()),
    path('content-publisher/',views.ContentPublisherCreateView.as_view()),
    path('admin/',views.AdminCreateView.as_view()),
    path('student-login/',views.Student_login_view),
    path('admin-login/',views.Admin_login_view),
    path('trainer-login/',views.Trainer_login_view),
    path('contentpublisher-login/',views.ContentPublisher_login_view),
    path('professional-login/',views.Professional_login_view),

    # URL FOR CONNECTIFYINDIA

    path('server-register/',views.ServerCreateView.as_view()),
    path('project-leader/',views.ProjectLeaderCreateView.as_view()),
    path('project-manager/',views.ProjectManagerCreateView.as_view()),
    path('content-publisher-connectify/',views.Content_PublisherCreateView.as_view()),
    path('connectify-admin/',views.ConnectifyAdminCreateView.as_view()),
    path('server-login/',views.Server_login_view),
    path('project-leader-login/',views.ProjectLeader_login_view),
    path('project-manager-login/',views.ProjectManager_login_view),
    path('connectify-content-publisher-login/',views.Content_Publisher_login_view),
    path('connectify-admin-login/',views.ConnectifyAdmin_login_view),


]