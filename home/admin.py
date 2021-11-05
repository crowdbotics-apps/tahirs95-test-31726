from django.contrib import admin

# Register your models here.
from .models import UserApp, Plan, Subscription

admin.site.register(UserApp)
admin.site.register(Plan)
admin.site.register(Subscription)