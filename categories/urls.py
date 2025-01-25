
from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name="categories"),
    path('create/', views.categoryCreate, name="createCategory"),
    path('update/<int:id>', views.categoryUpdate, name="updateCategory"),
    path('delete/<int:id>', views.deleteCategory, name="deleteCategory"),
]
