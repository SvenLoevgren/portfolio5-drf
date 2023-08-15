from rest_framework import serializers
from .models import Booking  # Import your models here, adjust the import if needed
from django.contrib.auth.models import User
from .models import MenuItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Customize the fields to be exposed in the API


class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Use the UserSerializer to include user details in the booking data

    class Meta:
        model = Booking
        fields = '__all__' 
# recommended fields if not using "all" = ['id', 'customer_name', 'email', 'phone_number', 'date', 'time', 'num_seats', 'user']


class MenuItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    description = serializers.CharField(source='get_description_display')

    class Meta:
        model = MenuItem
        fields = '__all__' 


# -------------------------------------For update API's only

class MenuItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        exclude = ['user', 'description']  # Exclude user field for updates
