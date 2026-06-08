from django.urls import path
from .views import CreateMonitorView, PauseMonitorView, PulseView, MonitorStatusView


urlpatterns = [
    path('', CreateMonitorView.as_view(), name='register-device'),
    path('<str:id>/heartbeat/', PulseView.as_view()),
    path('<str:id>/pause/', PauseMonitorView.as_view(), name='pause-monitor'),
    path('<str:id>/monitor-device/', MonitorStatusView.as_view(), name='monitor-a-device')
]