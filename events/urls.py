
from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name="events"),
    path('add-event/', views.addEvent, name="add-event")
]
