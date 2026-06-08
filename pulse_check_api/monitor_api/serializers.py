from .models import MonitorModel
from rest_framework import serializers

class MonitorSerializer(serializers.ModelSerializer):
    """ Serializers device data from model query to JSON format and vice versa"""
    class Meta:
        model = MonitorModel
        fields = ['id', 'timeout', 'alert_email']