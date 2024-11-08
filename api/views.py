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

    @action(detail=False, methods=['put'], url_path='update_status')
    def update_status(self, request):
        if not isinstance(request.data, list):
            return Response({'error': 'Expected a list of objects'}, status=status.HTTP_400_BAD_REQUEST)

        response_data = []
        for item in request.data:
            port_id = item.get("port_id")
            port_status = item.get("port_status")

            if port_id is None or port_status is None:
                response_data.append({
                    "port_id": port_id,
                    "status": "error",
                    "message": "Missing port_id or port_status"
                })
                continue

            try:
                port = Port.objects.get(port_id=port_id)
                port.port_status = port_status
                port.save()
                response_data.append({
                    "port_id": port_id,
                    "status": "updated",
                    "message": f"Port {port_id} status updated successfully"
                })
            except Port.DoesNotExist:
                response_data.append({
                    "port_id": port_id,
                    "status": "error",
                    "message": "Port not found"
                })

        return Response(response_data, status=status.HTTP_200_OK)

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