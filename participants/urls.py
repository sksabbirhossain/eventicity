
from django.urls import path
from . import views

urlpatterns = [
    path('', views.participants, name="participants"),
    path('create/', views.createParticipant, name="createParticipant"),
    path('update/<int:id>', views.updateParticipant, name="updateParticipant"),
    path('delete/<int:id>', views.deleteParticipant, name="deleteParticipant")
]
