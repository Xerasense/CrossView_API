# api/models.py

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from encrypted_model_fields.fields import EncryptedCharField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = EncryptedCharField(max_length=15)
    preferred_border_crossing = models.CharField(max_length=100)
    notification_threshold = models.IntegerField(default=30)

class EasyGoAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = EncryptedCharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

class BorderCrossing(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

class WaitTime(models.Model):
    border_crossing = models.ForeignKey(BorderCrossing, on_delete=models.CASCADE)
    direction = models.CharField(max_length=20)  # 'inbound' or 'outbound'
    wait_time = models.IntegerField()  # in minutes
    timestamp = models.DateTimeField(auto_now_add=True)

class CameraFeed(models.Model):
    border_crossing = models.ForeignKey(BorderCrossing, on_delete=models.CASCADE)
    url = models.URLField()
    last_analyzed = models.DateTimeField(null=True, blank=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)