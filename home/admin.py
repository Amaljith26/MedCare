from django.contrib import admin
from . models import Booking
# Register your models here.

@admin.register(Booking)
class AppointmentInfos(admin.ModelAdmin):
    list_display = ('name','age','phone','category','email','message')