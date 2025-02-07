from datacenter.models import Visit
from django.utils import timezone
from datetime import timedelta



SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600

visit = Visit(entered_at=timezone.now(), leaved_at=None)


def get_duration(visit):
    current_time = timezone.localtime()
    duration = (visit.leaved_at or current_time) - visit.entered_at
    return duration


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // SECONDS_IN_HOUR
    remainder = total_seconds % SECONDS_IN_HOUR
    minutes = remainder // SECONDS_IN_MINUTE
    seconds = remainder % SECONDS_IN_MINUTE
    return f'{hours}ч {minutes}мин {seconds}сек'


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration > timedelta(minutes=minutes)

