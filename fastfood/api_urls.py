from django.urls import path
from .views import BookingListAPIView

urlpatterns = [
    path('bookings/', BookingListAPIView.as_view(), name='booking-list'),
]