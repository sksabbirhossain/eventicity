from django.db import models
from events.models import Event

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    events = models.ManyToManyField(Event,related_name="participants")

    def __str__(self):
        return self.name