
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.categoryCreate, name="createCategory"),
    path('update/<int:id>', views.categoryUpdate, name="updateCategory"),
]
