from django.shortcuts import render
from django.contrib import messages
from .models import ContactForm
from .forms import ContactForm


# Create your views here.
def contact_us(request):
    """
    Renders the Contact page
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Thank you for your message! I will respond soon.")

    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {"contact_form": contact_form},
    )
