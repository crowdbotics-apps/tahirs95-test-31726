from django.db import models

from users.models import User
class UserApp(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        null=True,
        blank=True,
    )

class Plan(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()

class Subscription(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        related_name="plan",
        null=True,
        blank=True,
    )
    app = models.ForeignKey(
        UserApp,
        on_delete=models.CASCADE,
        related_name="app",
        null=True,
        blank=True,
    )