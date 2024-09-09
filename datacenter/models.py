from django.db import models
from django.utils.timezone import localtime
from datetime import timezone
import datetime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f"{self.owner_name} (inactive)"


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(f"leaved at {self.leaved_at}" if self.leaved_at else "not leaved"),
        )

    def get_duration(self):
        visit_time = (
            localtime(self.leaved_at) - localtime(self.entered_at)
        ).total_seconds()
        return visit_time

    def format_duration(self, visit_time):
        seconds = visit_time.total_seconds()
        hours = seconds // 3600

        int(hours)

        minutes = (seconds % 3600) // 60
        int(minutes)
        return f"{int(hours)}ч {int(minutes)}мин"

    def is_visit_long(self):
        now = datetime.datetime.now(timezone.utc)
        minutes = 60
        if self.leaved_at == None:
            duration = (now - localtime(self.entered_at)).total_seconds()
        else:
            duration = self.get_duration()
        return duration // 60 > minutes
