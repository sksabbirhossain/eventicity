from django.db import models
from categories.models import Category

# Create your models here.
class Event(models.Model):
    name= models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="events")

    def __str__(self):
        return self.name