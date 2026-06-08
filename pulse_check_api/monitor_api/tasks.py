import json
from datetime import timedelta
from django.utils import timezone
from .models import MonitorModel


def check_expired_monitors():

    now = timezone.now()

    monitors = MonitorModel.objects.filter(
        status=MonitorModel.STATUS.Healthy,
        alert_sent=False
    )

    for monitor in monitors:

        expiry_time = (
            monitor.last_beat +
            timedelta(seconds=monitor.timeout)
        )

        if now >= expiry_time:

            monitor.status = MonitorModel.STATUS.Down
            monitor.alert_sent = True

            monitor.save(
                update_fields=[
                    "status",
                    "alert_sent"
                ]
            )

            print(
                json.dumps(
                    {
                        "ALERT": f"Device {monitor.id} is down!",
                        "time": now.isoformat()
                    }
                )
            )