from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from treatments.models import Treatment 


# Create your models here.

TIME_SLOTS = [
    ("9 AM", "9 AM"),
    ("9:30 AM", "9:30 AM"),
    ("10 AM", "10 AM"),
    ("10:30 AM", "10:30 AM"),
    ("11 AM", "11 AM"),
    ("11:30 AM", "11:30 AM"),
    ("12 PM", "12 PM"),
    ("11:30 PM", "11:30 PM"),
    ("12 PM", "12 PM"),
    ("12:30 PM", "12:30 PM"),
    ("1 PM", "1 PM"),
    ("1:30 PM", "1:30 PM"),
    ("2 PM", "2 PM"),
    ("2:30 PM", "2:30 PM"),
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
]

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_SLOTS, default="9 AM")
    notes = models.TextField(blank=True, null=True) 
    created_on = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        """ Order appointments by date """
        ordering = ["-day"]
        unique_together = ['day', 'time']

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time} | treatment: {self.treatment.name}"
