from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EventForm 

# Create your views here.
def events(request):
    return render(request, "events/index.html")


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