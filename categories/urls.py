
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.categoryCreate, name="createCategory"),
]
