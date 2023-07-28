from django.contrib import admin
from .models import Booking
from .models import MenuItem


class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'phone_number', 'date', 'time', 'num_seats')


admin.site.register(Booking)


admin.site.register(MenuItem)
