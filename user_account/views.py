from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
class UserAccount(TemplateView):
    template_name = 'my_account/my_account.html'
