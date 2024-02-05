from django.urls import path
from .views import CustomUserCreate,AuthUserLoginView,UserListProfileView,change_password

app_name = 'users'
urlpatterns = [
    path('create/',CustomUserCreate.as_view(),name="create_user"),
    path('login/', AuthUserLoginView.as_view(), name ="login"),
    path('userprofile/', UserListProfileView.as_view(), name ="user-profile"),
    path('change_password/', change_password, name='change_password'),
    # path('logout/', NewRevokeTokenView.as_view(), name = "logout"),
    # path('auth/revoke-token/', RevokeTokenView.as_view(), name='revoke-token'),

]