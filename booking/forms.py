from .models import Appointment
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('first name', 'last name', 'email', 'phone number', 'treatment', 'day', 'time', 'notes')