# api/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, EasyGoAccount, BorderCrossing, WaitTime, CameraFeed, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'preferred_border_crossing', 'notification_threshold')

class EasyGoAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = EasyGoAccount
        fields = ('account_number', 'balance')

class BorderCrossingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorderCrossing
        fields = '__all__'

class WaitTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitTime
        fields = '__all__'

class CameraFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraFeed
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'