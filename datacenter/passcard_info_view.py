from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    def format_duration(duration):
        total_seconds = int(duration.total_seconds())
        hours = total_seconds // 3600
        remainder = total_seconds % 3600
        minutes = remainder // 60
        seconds = remainder % 60
        return f'{hours}ч {minutes}мин {seconds}сек'

    this_passcard_visits = []

    for visit in visits:
        duration = visit.get_duration()
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
            'is_strange': visit.is_visit_long()
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
