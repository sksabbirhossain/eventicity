from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def events(request):
    return render(request, "events/index.html")


# add event
def addEvent(request):
    return render(request,"add-event/index.html")