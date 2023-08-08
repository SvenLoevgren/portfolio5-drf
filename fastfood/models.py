from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator


class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone_number_regex = RegexValidator(regex=r'^\+?\d{1,3}[-\.\s]?\d{1,14}[-\.\s]?\d{1,14}$')
    phone_number = models.CharField(validators=[phone_number_regex], max_length=20)
    date = models.DateField()
    time = models.TimeField()
    num_seats = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Availability(models.Model):
    date = models.DateField()
    time = models.TimeField()
    max_seats_available = models.PositiveIntegerField()
    num_available_seats = models.PositiveIntegerField()


class MenuItem(models.Model):
    CATEGORY_CHOICES = (
        ('Rainbow Burgers', 'Rainbow Burgers'),
        ('No chicken Burgers', 'No chicken Burgers'),
        ('No chicken', 'No chicken'),
        ('Wraps', 'Wraps'),
        ('Wraps Dressings', 'Wraps Dressings'),
        ('Accessories', 'Accessories'),
        ('Desserts', 'Desserts'),
        ('Dip', 'Dip'),
        ('Drinks', 'Drinks'),
        ('Add-ons', 'Add-ons'),
        ('Snacks', 'Snacks'),
    )

    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
