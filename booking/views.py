from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import BookingForm
from .models import Appointment, Treatment
from datetime import datetime, timedelta

# Create your views here.

class BookingView(FormView):
    template_name = 'booking/booking.html'
    form_class = BookingForm
    success_url = reverse_lazy('my-account')  # Redirect after successful booking


    def check_availability(self, day, time, current_appointment=None):
        existing_appointments = Appointment.objects.filter(day=day, time=time)
        if current_appointment:
            existing_appointments = existing_appointments.exclude(pk=current_appointment.pk)
        return not existing_appointments.exists()


    def form_valid(self, form):
        # Extract data from the form
        cleaned_data = form.cleaned_data
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
                if Appointment.objects.filter(day=day).count() < 9:
                    if self.check_availability(day, time):
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


class BookingEdit(BookingView, UpdateView):
    """
    Edit an appointment
    """
    model = Appointment
    form_class = BookingForm
    template_name = 'booking/booking_edit.html'
    success_url = reverse_lazy('my-account')

    def get_object(self, queryset=None):
        return Appointment.objects.get(pk=self.kwargs['pk'], user=self.request.user)  # Ensures the logged in user owns the appointment

    def form_valid(self, form):

        # Exclude date and time fields from cleaned data
        cleaned_data = form.cleaned_data
        new_day = cleaned_data.get('day')
        new_time = cleaned_data.get('time')

        # Get the current appointment
        appointment = self.get_object()

        # Check if the new time and date are available
        if self.check_availability(new_day, new_time, current_appointment=appointment):
            appointment.treatment = cleaned_data['treatment']
            appointment.day = new_day
            appointment.time = new_time
            appointment.first_name = cleaned_data['first_name']
            appointment.last_name = cleaned_data['last_name']
            appointment.email = cleaned_data['email']
            appointment.phone_number = cleaned_data['phone_number']
            appointment.notes = cleaned_data['notes']
            appointment.save()

            messages.success(self.request, "Appointment updated successfully!")
            print("Redirecting to:", self.success_url)  # Debugging line
            return super().form_valid(form)

        form.add_error('time', 'Sorry, this time and date is already booked.')
        return self.form_invalid(form)

        


class DeleteBooking(DeleteView):
    """
    Delete an appointment
    """
    model = Appointment
    template_name = 'booking/booking_confirm_delete.html'
    success_url = reverse_lazy('my-account')

    def get_object(self, queryset=None):
        return Appointment.objects.get(pk=self.kwargs['pk'], user=self.request.user)  # Ensures the logged in user owns the appointment

    def delete(self, request, *args, **kwargs):
        appointment = self.get_object()
        print("Deleting appointment:", appointment)  # Debugging line
        messages.success(self.request, "Appointment deleted successfully!")
        
        return super().delete(request, *args, **kwargs)