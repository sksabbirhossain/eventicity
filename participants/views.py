from django.shortcuts import render, redirect
from .forms import ParticipantForm
from .models import Participant

# Create your views here.
def createParticipant(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = ParticipantForm()
    return render(request, "participant-form.html", {"form": form})


def updateParticipant(request, id):
    participants = Participant.objects.get(id = id)
    if request.method == "POST":
        form = ParticipantForm(request.POST, instance=participants)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = ParticipantForm(instance=participants)
    return render(request, "participant-form.html", {"form": form})