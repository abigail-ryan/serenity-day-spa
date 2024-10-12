from django.db import models
from django.utils import timezone


# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sent_on"]

    def __str__(self):
        return f"Contact from {self.name}"
