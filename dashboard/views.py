from django.shortcuts import render
from participants.models import Participant
from categories.models import Category
from events.models import Event
from django.db.models import Count,Q
from django.utils.timezone import now

# Create your views here.
def dashboard(request):
    # total participants
    participants = Participant.objects.all().count()

    categories = Category.objects.all()

    counts = Event.objects.aggregate(
        total=Count('id'),
        upcoming=Count('id', filter=Q(date__gt=now().date())),
        past=Count('id', filter=Q(date__lt=now().date()))
        )
    
    type = request.GET.get('type')
    category = request.GET.get('category')
    start = request.GET.get('start')
    end = request.GET.get('end')


    baseQuery = Event.objects.select_related('category').prefetch_related('participants')


    if type == 'events':
        events = baseQuery.all()
    elif type == 'upcoming':
        events = baseQuery.filter(date__gt=now().date())
    elif type == 'past':
        events = baseQuery.filter(date__lt=now().date())
    elif category and start and end :
        events = baseQuery.filter(
            Q(category__id=category) &  
            Q(date__gte=start) &      
            Q(date__lte=end) ).all()
    else:
        events = baseQuery.filter(date=now().date()).all()


    context = {
        "participants": participants,
        "categories": categories,
        "counts": counts,
        "events": events
    }
    return render(request, 'dashboard/index.html', context)