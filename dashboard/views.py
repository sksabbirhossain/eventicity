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

    if type == 'events':
        events = Event.objects.select_related('category').prefetch_related('events').all()
    elif type == 'upcoming':
        events = Event.objects.select_related('category').prefetch_related('upcoming').filter(date__gt=now().date())
    elif type == 'past':
        events = Event.objects.select_related('category').prefetch_related('past').filter(date__lt=now().date())


    context = {
        "participants": participants,
        "counts": counts,
        "events": events
    }
    return render(request, 'dashboard/index.html', context)