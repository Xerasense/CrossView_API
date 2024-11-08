from rest_framework import serializers
from .models import Port

# class ApiDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ApiData
#         fields = ['api_data_id', 'api_key']
#
# class SystemStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SystemStatus
#         fields = ['system_id', 'app_status', 'api_status', 'cam_status']
#
# class LogTableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LogTable
#         fields = '__all__'

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = [
            'port_id',
            'port_name',
            'location',
            'cam_north_link',
            'cam_south_link',
            'out_traffic_level',
            'in_traffic_level',
            'lane_us',
            'lane_status_mex',
            'us_lane_type',
        ]

# class UserSettingsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserSettings
#         fields = '__all__'
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'