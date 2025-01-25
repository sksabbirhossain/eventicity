
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createParticipant, name="createParticipant"),
    path('update/<int:id>', views.updateParticipant, name="updateParticipant"),
]
