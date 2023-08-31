from rest_framework import serializers
from .models import Booking
from django.contrib.auth.models import User
from .models import MenuItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Customize the fields to be exposed in the API
        fields = ['id', 'username', 'email']

# ------------------------------------------------------------------Bookings


class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Booking
        fields = '__all__'

# ------------------------------------------------------------------MenuItems

# ------------------------------------For the Menu Read API only (cRud)


class MenuItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    description = serializers.CharField(source='get_description_display')

    class Meta:
        model = MenuItem
        fields = '__all__'

# ------------------------------------For the Menu Create API only (Crud)


class MenuItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        exclude = ['user']

# ------------------------------------For the Menu update API only (crUd)


class MenuItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        # Exclude user field for updates
        exclude = ['user', 'description']
