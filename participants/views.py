from django.shortcuts import render, redirect
from .forms import ParticipantForm

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