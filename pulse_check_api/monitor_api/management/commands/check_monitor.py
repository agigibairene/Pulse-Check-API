from django.core.management.base import BaseCommand
from monitor_api.tasks import check_expired_monitors


class Command(BaseCommand):

    help = "Checks expired monitors"

    def handle(self, *args, **kwargs):
        check_expired_monitors()

        self.stdout.write(
            self.style.SUCCESS(
                "Monitor check completed."
            )
        )