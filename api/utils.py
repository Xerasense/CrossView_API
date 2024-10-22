# api/utils.py

import requests
from django.conf import settings
import boto3
from botocore.exceptions import ClientError

def fetch_cbp_data():
    url = settings.CBP_API_URL
    headers = {'X-API-Key': settings.CBP_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error
        return None

def analyze_camera_feed(feed_url):
    # Implement AI analysis of camera feed
    # This is a placeholder and should be replaced with actual AI model integration
    return {"traffic_level": "medium", "vehicle_count": 50}

def send_push_notification(user, message):
    # Implement push notification using FCM or another service
    # This is a placeholder and should be replaced with actual push notification logic
    print(f"Sending push  notification to {user.username}: {message}")

def get_s3_client():
    return boto3.client('s3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME
    )

def upload_file_to_s3(file, object_name=None):
    if object_name is None:
        object_name = file.name

    s3_client = get_s3_client()
    try:
        s3_client.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, object_name)
    except ClientError as e:
        print(e)
        return False
    return True

def get_file_from_s3(object_name):
    s3_client = get_s3_client()
    try:
        response = s3_client.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=object_name)
        return response['Body'].read()
    except ClientError as e:
        print(e)
        return None