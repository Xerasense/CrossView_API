from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PortViewSet

router = DefaultRouter()
# router.register(r'api-data', ApiDataViewSet)
# router.register(r'system-status', SystemStatusViewSet)
# router.register(r'logs', LogTableViewSet)
router.register(r'ports', PortViewSet)
# router.register(r'user-settings', UserSettingsViewSet)
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]