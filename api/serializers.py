from rest_framework import serializers
from .models import ApiData, SystemStatus, LogTable, Port, UserSettings, User

class ApiDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiData
        fields = '__all__'

class SystemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemStatus
        fields = '__all__'

class LogTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogTable
        fields = '__all__'

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = '__all__'

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'