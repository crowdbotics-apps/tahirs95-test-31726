from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({"OK", "Auth Token is deleted."}, status=status.HTTP_200_OK)

@api_view(["POST"])
def register(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    email_check = User.objects.filter(email=email)
    if email_check:
        return Response(
            {"Error": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST
        )
    user = User.objects.create(
        username=email, email=email, name=name
    )
    user.set_password(password)
    user.save()
    return Response({
        'name': user.name,
        'email': user.email,
    }, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def change_password(request):
    email = request.POST.get("email")
    password1 = request.POST.get("password1")
    password2 = request.POST.get("password2")
    if password1 != password2:
        return Response(
            {"error": "password not matched"}, status=status.HTTP_400_BAD_REQUEST
        )
    user = User.objects.filter(email=email)
    if user:
        user.set_password(password1)
        user.save()
        return Response({"OK": "password is reset."}, status=status.HTTP_201_CREATED)
    else:
        return Response(
            {"Error": "User doesn't exist."}, status=status.HTTP_400_BAD_REQUEST
        )