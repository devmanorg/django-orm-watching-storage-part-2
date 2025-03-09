from django.utils import timezone


SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600


def get_duration(visit):
    entered_at_local = timezone.localtime(visit.entered_at)
    leaved_at_local = timezone.localtime(visit.leaved_at) \
        if visit.leaved_at \
        else timezone.localtime()

    duration = leaved_at_local - entered_at_local
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
    return duration.total_seconds > minutes * SECONDS_IN_MINUTE

