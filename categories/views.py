from django.shortcuts import render, redirect, HttpResponse
from .models import Category
from .forms import CategoryForm

# Create your views here.
def categoryCreate(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = CategoryForm()
    return render(request, "category-form.html", {"form": form})



def categoryUpdate(request, id):
    category =Category.objects.get(id = id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = CategoryForm(instance=category)
    return render(request, "category-form.html", {"form": form})

