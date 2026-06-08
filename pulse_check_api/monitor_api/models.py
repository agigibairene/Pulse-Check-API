from django.db import models

class MonitorModel(models.Model):
    
    class STATUS(models.TextChoices):
        Healthy = 'active', 'Active'
        Paused = 'paused', 'Paused'
        Down = 'down', 'Down'
        
    id = models.CharField(max_length=150, primary_key=True)
    timeout = models.IntegerField()
    alert_email = models.EmailField()
    alert_sent = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS.choices, default=STATUS.Healthy)
    last_beat = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    