from django.shortcuts import render, redirect
from .forms import ParticipantForm
from .models import Participant

# Create your views here.
def participants(request):
    participants = Participant.objects.all()
    return render(request, "participants.html", {"participants": participants})

def createParticipant(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("participants")
    else:
        form = ParticipantForm()
    return render(request, "participant-form.html", {"form": form})


def updateParticipant(request, id):
    participants = Participant.objects.get(id = id)
    if request.method == "POST":
        form = ParticipantForm(request.POST, instance=participants)
        if form.is_valid():
            form.save()
            return redirect("participants")
    else:
        form = ParticipantForm(instance=participants)
    return render(request, "participant-form.html", {"form": form})


def deleteParticipant(request, id):
    if request.method == "POST":
        event = Participant.objects.get(id = id)
        event.delete()
        return redirect('participants')
    else:
        return redirect('participants')