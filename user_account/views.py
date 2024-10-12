from django.shortcuts import render
from django.views.generic import TemplateView
from booking.models import Appointment


# Create your views here.
class UserAccount(TemplateView):
    template_name = 'my_account/my_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['appointments'] = Appointment.objects.filter(user=user)

        return context
