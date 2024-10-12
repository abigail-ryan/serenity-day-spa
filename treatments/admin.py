from django.contrib import admin
from .models import Treatment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Treatment)
class TreatmentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'price', 'status')
    search_fields = ['name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description', 'requirements_details',)
