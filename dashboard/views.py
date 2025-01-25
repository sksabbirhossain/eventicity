from django.shortcuts import render
from participants.models import Participant
from events.models import Event
from django.db.models import Count,Q
from django.utils.timezone import now

# Create your views here.
def dashboard(request):
    # total participants
    participants = Participant.objects.all().count()

    counts = Event.objects.aggregate(
        total=Count('id'),
        upcoming=Count('id', filter=Q(date__gt=now().date())),
        past=Count('id', filter=Q(date__lt=now().date()))
        )
    
    type = request.GET.get('type', 'events')

    baseQuery = Event.objects.select_related('category')

    if type == 'events':
        events = baseQuery.all()
    elif type == 'upcoming':
        events = baseQuery.filter(date__gt=now().date())
    elif type == 'past':
        events = baseQuery.filter(date__lt=now().date())


    context = {
        "participants": participants,
        "counts": counts,
        "events": events
    }
    return render(request, 'dashboard/index.html', context)