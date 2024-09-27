from django.contrib import admin
from .models import ContactForm
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(ContactForm)
class ContactForm(admin.ModelAdmin):

    list_display = ('name', 'message', 'read', 'sent_on',)