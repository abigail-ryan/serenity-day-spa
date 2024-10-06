from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import BookingForm
from .models import Appointment, Treatment
from datetime import datetime, timedelta

# Create your views here.

class BookingView(FormView):
    template_name = 'booking/booking.html'
    form_class = BookingForm
    success_url = reverse_lazy('my-account')  # Redirect after successful booking

    def form_valid(self, form):
        # Extract data from the form
        treatment = form.cleaned_data['treatment']
        day = form.cleaned_data['day']
        time = form.cleaned_data['time']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        notes = form.cleaned_data['notes']

        #  checking availability
        today = datetime.now()
        min_date = today.strftime('%d-%m-%Y')
        max_date = (today + timedelta(days=21)).strftime('%d-%m-%Y')

        if min_date <= day.strftime('%d-%m-%Y') <= max_date:
            if day.weekday() in [1, 2, 3, 4, 5]:  # Tuesday, Wednesday, Thursday, Friday, Saturday
                if Appointment.objects.filter(day=day).count() < 10:
                    if not Appointment.objects.filter(day=day, time=time).exists():
                        # Create the appointment
                        Appointment.objects.create(
                            user=self.request.user,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            phone_number=phone_number,
                            treatment=treatment,
                            day=day,
                            time=time,
                            notes=notes
                        )
                        messages.success(self.request, "Appointment Saved!")
                        return super().form_valid(form)
                    else:
                        messages.error(self.request, "Sorry, the selected time is already booked!")
                else:
                    messages.error(self.request, "Sorry, the selected date is full!")
            else:
                messages.error(self.request, "Sorry, the selected date is incorrect.")
        else:
            messages.error(self.request, "Sorry, the selected date isn't in the correct time period!")

        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['treatments'] = Treatment.objects.all()
        context['weekdays'] = [(datetime.now() + timedelta(days=i)).strftime('%d-%m-%Y') for i in range(22)]
        context['times'] = [
            "9 AM", "9:30 AM", "10 AM", "10:30 AM", "11 AM", 
            "11:30 AM", "12 PM", "12:30 PM", "1 PM", "1:30 PM",
            "2 PM", "2:30 PM", "3 PM", "3:30 PM", "4 PM",
            "4:30 PM", "5 PM", "5:30 PM"
        ]
        return context




# def booking(request):
#     # Generate a list of the next 21 days and get all available treatments
#     today = datetime.now()
#     weekdays = [(today + timedelta(days=i)).strftime('%d-%m-%Y') for i in range(22)]
#     treatments = Treatment.objects.all()

#     TIME_SLOTS = [
#         "9 AM", "9:30 AM", "10 AM", "10:30 AM", "11 AM", 
#         "11:30 AM", "12 PM", "12:30 PM", "1 PM", "1:30 PM",
#         "2 PM", "2:30 PM", "3 PM", "3:30 PM", "4 PM",
#         "4:30 PM", "5 PM", "5:30 PM"
#     ]

#     if request.method == 'POST':
#         treatment_id = request.POST.get('treatment')
#         day_str = request.POST.get('day')
#         time = request.POST.get('time')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phone_number')
#         notes = request.POST.get('notes', '')

#         if not treatment_id:
#             messages.error(request, "Please select a Treatment!")
#             return redirect('booking/booking.html')

#         # Fetch the treatment instance
#         try:
#             treatment = Treatment.objects.get(id=treatment_id)
#         except Treatment.DoesNotExist:
#             messages.error(request, "Selected treatment does not exist.")
#             return redirect('booking/booking.html')

#         try:
#             day = datetime.strptime(day_str, '%d-%m-%Y')  # Convert string to datetime
#         except ValueError:
#             messages.error(request, "Invalid date format.")
#             return redirect('booking/booking.html')

#         # Validate date and time
#         minDate = today.strftime('%d-%m-%Y')
#         maxDate = (today + timedelta(days=21)).strftime('%d-%m-%Y')

#         if minDate <= day_str <= maxDate:
#             if day.weekday() in [0, 2, 5]:  # Monday (0), Wednesday (2), Saturday (5)
#                 if Appointment.objects.filter(day=day).count() < 10:
#                     if not Appointment.objects.filter(day=day, time=time).exists():
#                         # Create the appointment with all required fields
#                         Appointment.objects.create(
#                             user=request.user,
#                             first_name=first_name,
#                             last_name=last_name,
#                             email=email,
#                             phone_number=phone_number,
#                             treatment=treatment,
#                             day=day,
#                             time=time,
#                             notes=notes
#                         )
#                         messages.success(request, "Appointment Saved!")
#                         return redirect('my-account')
#                     else:
#                         messages.error(request, "Sorry, the selected time is already booked!")
#                 else:
#                     messages.error(request, "Sorry, the selected date is full!")
#             else:
#                 messages.error(request, "Sorry, the selected date is incorrect.")
#         else:
#             messages.error(request, "Sorry, the selected date isn't in the correct time period!")

#     return render(request, 'booking/booking.html', {
#         'weekdays': weekdays,
#         'treatments': treatments,
#         'times': TIME_SLOTS,
#     })