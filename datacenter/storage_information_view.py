from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime



def storage_information_view(request):
    
    active_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in active_visits:
        name_visit = visit.passcard.owner_name
        time_entered_at = localtime(visit.entered_at)
        duration = visit.get_duration()
        non_closed_visits.append(
            {
                'who_entered': name_visit,
                'entered_at': time_entered_at,
                'duration': visit.format_duration(duration),
                'is_strange': visit.is_visit_long()
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
