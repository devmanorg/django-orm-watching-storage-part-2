from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    leaved_at_visits = Visit.objects.filter(leaved_at=None)

    def format_duration(duration):
        total_seconds = int(duration.total_seconds())
        hours = total_seconds // 3600
        remainder = total_seconds % 3600
        minutes = remainder // 60
        return f'{hours}ч {minutes}мин'

    non_closed_visits = []
    for visit in leaved_at_visits:
        duration = visit.get_duration()
        visit_info = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at.strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(duration),
        }
        non_closed_visits.append(visit_info)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
