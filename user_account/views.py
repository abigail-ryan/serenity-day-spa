from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class UserAccount(View):
    def get(self, request):
        return HttpResponse("This is your account page")