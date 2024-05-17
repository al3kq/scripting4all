from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_subscription_status = models.CharField(max_length=20, default='inactive')  # Add this line