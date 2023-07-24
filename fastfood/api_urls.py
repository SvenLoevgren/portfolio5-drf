from django.urls import path
from .views import BookingListCreateAPIView, BookingDetailAPIView

urlpatterns = [
    path('bookings/', BookingListCreateAPIView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetailAPIView.as_view(), name='booking-detail'),
]
