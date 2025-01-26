from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EventForm 
from .models import Event
from categories.models import Category
from django.db.models import Count,Q
from django.utils.timezone import now

# Create your views here.
def events(request):
    
    categories = Category.objects.all()

    category = request.GET.get('category')
    start = request.GET.get('start')
    end = request.GET.get('start')
    
    baseQuery = Event.objects.select_related('category').prefetch_related('participants')

    if category and start and end :
        events = baseQuery.filter(
            Q(category__id=category) &  
            Q(date__gte=start) &      
            Q(date__lte=end) ).all()
    else:
        events = baseQuery.all()
    

    context ={
        "events":events,
        "categories": categories
    }
    return render(request, "events/index.html", context)


def detailsEvent(request, id):
    events = Event.objects.select_related('category').prefetch_related('participants').filter(id=id).all()
    return render(request, "details.html", {"events": events})

# add event
def addEvent(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = EventForm()
    return render(request,"event-form.html", {"form": form})


def updateEvent(request, id):
    events = Event.objects.get(id = id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=events)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = EventForm(instance=events)
    return render(request,"event-form.html", {"form": form})


def deleteEvent(request, id):
    if request.method == "POST":
        event = Event.objects.get(id = id)
        event.delete()
        return redirect('dashboard')
    else:
        return redirect('dashboard')