from django.db import models

# class ApiData(models.Model):
#     api_data_id = models.AutoField(primary_key=True)
#     api_key = models.CharField(max_length=255, null=True)
#
# class SystemStatus(models.Model):
#     system_id = models.AutoField(primary_key=True)
#     app_status = models.CharField(max_length=255, null=True)
#     api_status = models.CharField(max_length=255, null=True)
#     cam_status = models.CharField(max_length=255, null=True)

# class LogTable(models.Model):
#     log_id = models.AutoField(primary_key=True)
#     event_type = models.CharField(max_length=255, null=True)
#     timestamp = models.DateTimeField(null=True)
#     system = models.ForeignKey(SystemStatus, on_delete=models.CASCADE, null=True)

class Port(models.Model):
    port_id = models.AutoField(primary_key=True)
    port_name = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    cam_north_link = models.CharField(max_length=255, null=True)
    cam_south_link = models.CharField(max_length=255, null=True)
    out_traffic_level = models.CharField(max_length=50, null=True)
    in_traffic_level = models.CharField(max_length=50, null=True)
    lane_us = models.CharField(max_length=255, null=True)
    lane_status_mex = models.CharField(max_length=255, null=True)
    us_lane_type = models.CharField(max_length=255, null=True)

# class UserSettings(models.Model):
#     user_settings_id = models.AutoField(primary_key=True)
#
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     wtu_data = models.CharField(max_length=255, null=True)
#     user_settings = models.ForeignKey(UserSettings, on_delete=models.CASCADE, null=True)