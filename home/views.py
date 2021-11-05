from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view

from .serializers import SubscriptionSerializer, UserAppSerializer
from .models import UserApp, Subscription, Plan
class ListUserAppAPIView(ListAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializer

    def get_queryset(self):
        user = self.request.user
        return UserApp.objects.filter(user=user)

class CreateUserAppAPIView(CreateAPIView):
    serializer_class = UserAppSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return UserApp.objects.filter(user=user)

class UpdateUserAppAPIView(UpdateAPIView):
    serializer_class = UserAppSerializer

    def get_queryset(self):
        user = self.request.user
        return UserApp.objects.filter(user=user)

class DeleteUserAppAPIView(DestroyAPIView):
    serializer_class = UserAppSerializer

    def get_queryset(self):
        user = self.request.user
        return UserApp.objects.filter(user=user)

class RetrieveSubscriptionAPIView(RetrieveAPIView):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        user = self.request.user
        return Subscription.objects.filter(app__user=user)
class UpdateSubscriptionAPIView(UpdateAPIView):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        user = self.request.user
        return Subscription.objects.filter(app__user=user)

@api_view(['POST'])
def associate_plan(request, pk):
    sub_id = request.GET.get('id')
    plan_id = request.POST.get('plan_id')
    if sub_id and plan_id:
        subscription = Subscription.objects.filter(id=sub_id)
        plan = Plan.objects.filter(id=plan_id).first()
        subscription.plan = plan
        subscription.save()
        return JsonResponse({'message': 'Plan associated.'})
    return JsonResponse({'message': 'Plan not associated'}, status=status.HTTP_404_NOT_FOUND) 

def home(request):
    packages = [
	{'name':'django-allauth', 'url': 'https://pypi.org/project/django-allauth/0.38.0/'},
	{'name':'django-bootstrap4', 'url': 'https://pypi.org/project/django-bootstrap4/0.0.7/'},
	{'name':'djangorestframework', 'url': 'https://pypi.org/project/djangorestframework/3.9.0/'},
    ]
    context = {
        'packages': packages
    }
    return render(request, 'home/index.html', context)
