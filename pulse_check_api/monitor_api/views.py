from rest_framework import generics, status
from .serializers import MonitorSerializer
from .models import MonitorModel
from rest_framework.response import Response


class CreateMonitorView(generics.ListCreateAPIView):
    """ Allows user to retrieve all devices and all register a device"""
    queryset = MonitorModel.objects.all()
    serializer_class = MonitorSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        monitor = serializer.save()

        return Response(
            {'message': f"Monitor {monitor.id} successfully created "},
            status=status.HTTP_201_CREATED
        )
        
    