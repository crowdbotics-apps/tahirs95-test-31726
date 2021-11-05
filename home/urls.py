from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.ListUserAppAPIView.as_view(), name="list_apps"),
    path("create/", views.CreateUserAppAPIView.as_view(), name="create_app"),
    path("update/<int:pk>/", views.UpdateUserAppAPIView.as_view(), name="update_app"),
    path("delete/<int:pk>/",views.DeleteUserAppAPIView.as_view(), name="delete_app"),
    path("sub_retrieve/<int:pk>/", views.RetrieveSubscriptionAPIView.as_view(), name="retrieve_sub"),
    path("update_sub/<int:pk>/", views.UpdateSubscriptionAPIView.as_view(), name="update_sub"),
    path("associate_plan/", views.associate_plan, name="associate_plan"),
]
