from rest_framework import generics, status
from .serializers import MonitorSerializer
from .models import MonitorModel
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone


class CreateMonitorView(generics.ListCreateAPIView):
    """ Allows user to retrieve all devices and all register a device"""
    queryset = MonitorModel.objects.all()
    serializer_class = MonitorSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        monitor = serializer.save()

        return Response(
            {'message': f"Monitor {monitor.id} successfully created"},
            status=status.HTTP_201_CREATED
        )
        


class PulseView(generics.GenericAPIView):
    
    def post(self, request, id):
        
        monitor = get_object_or_404(MonitorModel, id=id)
        
        monitor.last_beat = timezone.now()
        monitor.status = MonitorModel.STATUS.Healthy
        monitor.alert_sent = False
        monitor.save()
        
        return Response(
            {"message": "Heartbeat received"}
        )
        


class PauseMonitorView(generics.GenericAPIView):
    """ Allows user to pause the beat/monitor"""
    def post(self, request, id):
        monitor = get_object_or_404(MonitorModel, id=id)
        
        monitor.status = MonitorModel.STATUS.Paused
        monitor.save(update_fields=['status'])
        return Response(
            {"message": "Monitor paused"}
        )
        

class MonitorStatusView(generics.GenericAPIView):
    """ Monitors the status of a specific device"""
    def get(self, request, id):

        monitor = get_object_or_404(MonitorModel,id=id)

        return Response({
            "id": monitor.id,
            "status": monitor.status,
            "timeout": monitor.timeout,
            "last_beat": monitor.last_beat,
            "alert_email": monitor.alert_email,
        })