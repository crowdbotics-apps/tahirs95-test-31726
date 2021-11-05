from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
    register,
    change_password,
    logout
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('rest-auth/login/', obtain_auth_token, name='api_token_auth'),
    path('rest-auth/registration/', register, name='register'),
    path('rest-auth/password/change/', change_password, name='change_password'),
    path('rest-auth/logout/', logout, name='logout'),

]
