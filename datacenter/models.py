from django.db import models
from django.utils import timezone
from datetime import timedelta


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(visit):
        current_time = timezone.localtime()

        if visit.leaved_at:
            duration = visit.leaved_at - visit.entered_at
        else:
            duration = current_time - visit.entered_at

        return (duration)

    def is_visit_long(visit, minutes=60):
        duration = visit.get_duration()
        return duration > timedelta(minutes=minutes)