from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date','time','location', 'category']

    # Custom Date Field
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    # Custom Time Field
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )