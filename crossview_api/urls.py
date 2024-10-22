# crossview_api/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    UserViewSet, UserProfileViewSet, EasyGoAccountViewSet,
    BorderCrossingViewSet, WaitTimeViewSet, CameraFeedViewSet,
    NotificationViewSet, CustomTokenObtainPairView
)
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'easygo', EasyGoAccountViewSet)
router.register(r'border-crossings', BorderCrossingViewSet)
router.register(r'wait-times', WaitTimeViewSet)
router.register(r'camera-feeds', CameraFeedViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]