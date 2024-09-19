from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Treatment(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=False)
    excerpt = models.CharField(max_length=250, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    has_requirements = models.BooleanField(default=False)
    requirements_details = models.CharField(max_length=250)
    status = models.IntegerField(choices=STATUS, default=0)