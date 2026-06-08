from django.urls import path
from .views import CreateMonitorView


urlpatterns = [
    path('', CreateMonitorView.as_view(), name='register-device')
]