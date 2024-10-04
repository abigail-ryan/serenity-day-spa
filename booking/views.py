from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import Appointment  
from treatments.models import Treatment  
from django.contrib import messages

# Create your views here.

def booking(request):
    # Generate a list of the next 21 days and get all available treatments
    today = datetime.now()
    weekdays = [(today + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(22)]
    treatments = Treatment.objects.all()

    TIME_SLOTS = [
        "9 AM", "9:30 AM", "10 AM", "10:30 AM", "11 AM", 
        "11:30 AM", "12 PM", "12:30 PM", "1 PM", "1:30 PM",
        "2 PM", "2:30 PM", "3 PM", "3:30 PM", "4 PM",
        "4:30 PM", "5 PM", "5:30 PM"
    ]

    if request.method == 'POST':
        treatment_id = request.POST.get('treatment')
        day_str = request.POST.get('day')
        time = request.POST.get('time')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        notes = request.POST.get('notes', '')

        if not treatment_id:
            messages.error(request, "Please select a Treatment!")
            # return redirect('booking')

        # Fetch the treatment instance
        try:
            treatment = Treatment.objects.get(id=treatment_id)
        except Treatment.DoesNotExist:
            messages.error(request, "Selected treatment does not exist.")
            # return redirect('booking/booking.html')

        try:
            day = datetime.strptime(day_str, '%Y-%m-%d')  # Convert string to datetime
        except ValueError:
            messages.error(request, "Invalid date format.")
            # return redirect('booking/booking.html')

        # Validate date and time
        minDate = today.strftime('%Y-%m-%d')
        maxDate = (today + timedelta(days=21)).strftime('%Y-%m-%d')

        if minDate <= day_str <= maxDate:
            if day.weekday() in [0, 2, 5]:  # Monday (0), Wednesday (2), Saturday (5)
                if Appointment.objects.filter(day=day).count() < 10:
                    if not Appointment.objects.filter(day=day, time=time).exists():
                        # Create the appointment with all required fields
                        Appointment.objects.create(
                            user=request.user,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            phone_number=phone_number,
                            treatment=treatment,
                            day=day,
                            time=time,
                            notes=notes
                        )
                        messages.success(request, "Appointment Saved!")
                        return redirect('my-account')
                    else:
                        messages.error(request, "Sorry, the selected time is already booked!")
                else:
                    messages.error(request, "Sorry, the selected date is full!")
            else:
                messages.error(request, "Sorry, the selected date is incorrect.")
        else:
            messages.error(request, "Sorry, the selected date isn't in the correct time period!")

    return render(request, 'booking/booking.html', {
        'weekdays': weekdays,
        'treatments': treatments,
        'times': TIME_SLOTS,
    })