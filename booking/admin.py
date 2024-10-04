from django.contrib import admin
from .models import Appointment


# Register your models here.
@admin.register(Appointment)
class Appointment(admin.ModelAdmin):

    list_display = ('get_full_name', 'treatment', 'day', 'time',)

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    get_full_name.short_description = 'Name' 