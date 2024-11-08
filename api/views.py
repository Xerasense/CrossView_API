from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Port, TrafficAllowed
from .serializers import PortSerializer, TrafficAllowedSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
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

class PortViewSet(ModelViewSet):
    # Just need to add some filtering capabilities
    queryset = Port.objects.all()
    serializer_class = PortSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['port_id', 'port_name', 'location']
    # permission_classes = [permissions.IsAuthenticated]
    @action(detail=True, methods=['get'], url_path='portstatus')
    def port_status(self, request, pk=None):
        try:
            port = Port.objects.get(pk=pk)
            traffic_status = TrafficAllowed.objects.get(port_id=port)  # Fetch TrafficAllowed using Port
            serializer = TrafficAllowedSerializer(traffic_status)
            return Response(serializer.data)
        except Port.DoesNotExist:
            return Response({'error': 'Port not found'}, status=status.HTTP_404_NOT_FOUND)
        except TrafficAllowed.DoesNotExist:
            return Response({'error': 'PortStatus not found'}, status=status.HTTP_404_NOT_FOUND)

class TrafficAllowedViewSet(ModelViewSet):
    queryset = TrafficAllowed.objects.all()
    serializer_class = TrafficAllowedSerializer



# class UserSettingsViewSet(viewsets.ModelViewSet):
#     queryset = UserSettings.objects.all()
#     serializer_class = UserSettingsSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]