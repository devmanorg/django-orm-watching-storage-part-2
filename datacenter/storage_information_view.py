from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.time_utils import format_duration, get_duration

def storage_information_view(request):
    leaved_at_visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for visit in leaved_at_visits:
        duration = get_duration()
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
