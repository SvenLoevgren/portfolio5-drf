from django.urls import path
from .views import BookingListCreateAPIView, BookingDetailAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('bookings/', BookingListCreateAPIView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetailAPIView.as_view(), name='booking-detail'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
