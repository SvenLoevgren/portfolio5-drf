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


class MenuItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    description = serializers.CharField(source='get_description_display')

    class Meta:
        model = MenuItem
        fields = '__all__' 


class MenuItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title', 'name', 'price', 'quantity', 'description']

# -------------------------------------For the update API only (crUd)


class MenuItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        exclude = ['user', 'description']  # Exclude user field for updates
