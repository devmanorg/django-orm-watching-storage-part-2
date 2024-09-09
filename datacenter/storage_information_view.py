from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import timezone
import datetime


def storage_information_view(request):
    non_closed_visits = []
    not_leaved_visit = Visit.objects.filter(leaved_at=None)
    now = datetime.datetime.now(timezone.utc)

    for visit in not_leaved_visit:
        entered = localtime(visit.entered_at)

        non_closed_visits.append(
            {
                "who_entered": visit.passcard.owner_name,
                "entered_at": entered,
                "duration": visit.format_duration(now - entered),
                "is_strange": visit.is_visit_long(),
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, "storage_information.html", context)
