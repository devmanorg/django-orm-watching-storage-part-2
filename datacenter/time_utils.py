from datacenter.models import Visit
from django.utils import timezone
from datetime import timedelta


visit = Visit(entered_at=timezone.now(), leaved_at=None)


def get_duration(visit):
    current_time = timezone.localtime()

    if visit.leaved_at:
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = current_time - visit.entered_at

    return (duration)


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    remainder = total_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return f'{hours}ч {minutes}мин {seconds}сек'


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration > timedelta(minutes=minutes)

