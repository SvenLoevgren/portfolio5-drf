from django.contrib import admin
from .models import Booking
# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'phone_number', 'date', 'time', 'num_seats')


admin.site.register(Booking)