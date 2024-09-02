from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from datetime import timezone
import datetime


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        entered = localtime(visit.entered_at)
        leave = localtime(visit.leaved_at)

        this_passcard_visits.append(
            {
                "entered_at": entered,
                "duration": visit.format_duration(leave - entered),
                "is_strange": visit.is_visit_long(),
            }
        )

    context = {"passcard": passcard, "this_passcard_visits": this_passcard_visits}
    return render(request, "passcard_info.html", context)
