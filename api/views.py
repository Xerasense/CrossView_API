from rest_framework import viewsets, permissions
from .models import Port
from .serializers import PortSerializer
# class ApiDataViewSet(viewsets.ModelViewSet):
#     queryset = ApiData.objects.all()
#     serializer_class = ApiDataSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
# class SystemStatusViewSet(viewsets.ModelViewSet):
#     queryset = SystemStatus.objects.all()
#     serializer_class = SystemStatusSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class LogTableViewSet(viewsets.ModelViewSet):
#     queryset = LogTable.objects.all()
#     serializer_class = LogTableSerializer
#     permission_classes = [permissions.IsAuthenticated]

class PortViewSet(viewsets.ModelViewSet):
    # Just need to add some filtering capabilities
    queryset = Port.objects.all()
    serializer_class = PortSerializer
    # permission_classes = [permissions.IsAuthenticated]

# class UserSettingsViewSet(viewsets.ModelViewSet):
#     queryset = UserSettings.objects.all()
#     serializer_class = UserSettingsSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]