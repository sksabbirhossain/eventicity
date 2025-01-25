
from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name="events"),
    path('add-event/', views.addEvent, name="add-event"),
    path('details/<int:id>', views.detailsEvent, name="detailsEvent"),
    path('update/<int:id>', views.updateEvent, name="updateEvent"),
    path('delete/<int:id>', views.deleteEvent, name="deleteEvent")
]
