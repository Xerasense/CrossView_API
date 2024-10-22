# api/views.py

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .models import UserProfile, EasyGoAccount, BorderCrossing, WaitTime, CameraFeed, Notification
from .serializers import (
    UserSerializer, UserProfileSerializer, EasyGoAccountSerializer,
    BorderCrossingSerializer, WaitTimeSerializer, CameraFeedSerializer, NotificationSerializer
)
from .utils import fetch_cbp_data, analyze_camera_feed, send_push_notification
import boto3
from django.conf import settings

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User created successfully"
        }, status=status.HTTP_201_CREATED)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

class EasyGoAccountViewSet(viewsets.ModelViewSet):
    queryset = EasyGoAccount.objects.all()
    serializer_class = EasyGoAccountSerializer

    def get_queryset(self):
        return EasyGoAccount.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def reload_funds(self, request, pk=None):
        account = self.get_object()
        amount = request.data.get('amount')
        if amount:
            account.balance += float(amount)
            account.save()
            return Response({"message": "Funds added successfully"})
        return Response({"error": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)

class BorderCrossingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BorderCrossing.objects.all()
    serializer_class = BorderCrossingSerializer

class WaitTimeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WaitTime.objects.all()
    serializer_class = WaitTimeSerializer

    @action(detail=False, methods=['get'])
    def update_wait_times(self, request):
        cbp_data = fetch_cbp_data()
        # Process and save CBP data
        # Update WaitTime objects
        return Response({"message": "Wait times updated successfully"})

class CameraFeedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CameraFeed.objects.all()
    serializer_class = CameraFeedSerializer

    @action(detail=True, methods=['get'])
    def analyze(self, request, pk=None):
        camera_feed = self.get_object()
        analysis_result = analyze_camera_feed(camera_feed.url)
        # Process and save analysis result
        return Response(analysis_result)

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def send_push(self, request):
        user = request.user
        message = request.data.get('message')
        if message:
            send_push_notification(user, message)
            return Response({"message": "Push notification sent"})
        return Response({"error": "Invalid message"}, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = User.objects.get(username=request.data['username'])
            response.data['user_id'] = user.id
        return response