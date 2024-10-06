from django import forms
from .models import Appointment, Treatment, TIME_SLOTS

class BookingForm(forms.Form):
    treatment = forms.ModelChoiceField(queryset=Treatment.objects.all())
    day = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.ChoiceField(choices=TIME_SLOTS)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    notes = forms.CharField(required=False, widget=forms.Textarea)