from . import views
from django.urls import path

urlpatterns = [
    path('contact/', views.contact_us, name='contact'),
]