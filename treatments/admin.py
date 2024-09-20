from django.contrib import admin
from .models import Treatment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Treatment)
class TreatmentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'status')
    search_fields = ['name',]
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description', 'excerpt', 'price', 'duration', 'has_requirements', 'requirements_details',)


# Register your models here.

