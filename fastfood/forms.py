from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=20, error_messages={'invalid': 'Please enter a valid phone number, country code and then without the first zero. ie. +46-709999999'})

    class Meta:
        model = Booking
        fields = ['customer_name', 'email', 'phone_number', 'date', 'time', 'num_seats']
