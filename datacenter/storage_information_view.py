from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):

    remaining_visitors = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visitor in remaining_visitors:
        visitors = {
            'who_entered': visitor.passcard,
            'entered_at': visitor.entered_at,
            'duration': visitor.get_duration(),
            'is_strange': visitor.is_long()
        }
        non_closed_visits.append(visitors)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }

    return render(request, 'storage_information.html', context)
