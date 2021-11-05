from rest_framework import serializers
from .models import UserApp, Subscription

class UserAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApp
        fields = ('name', 'description')

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('name', 'description', 'plan')