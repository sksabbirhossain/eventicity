from django.shortcuts import render, redirect, HttpResponse
from .models import Category
from .forms import CategoryForm

# Create your views here.

def categories(request):
    categories = Category.objects.all()
    return render(request, "index.html", {"categories": categories})

def categoryCreate(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categories")
    else:
        form = CategoryForm()
    return render(request, "category-form.html", {"form": form})



def categoryUpdate(request, id):
    category =Category.objects.get(id = id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories")
    else:
        form = CategoryForm(instance=category)
    return render(request, "category-form.html", {"form": form})



def deleteCategory(request, id):
    if request.method == "POST":
        event = Category.objects.get(id = id)
        event.delete()
        return redirect('categories')
    else:
        return redirect('categories')

