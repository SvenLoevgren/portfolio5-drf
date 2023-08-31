from django.contrib import admin
from .views import (
    fastfood_home, booking, contactus, booking_list, edit_booking,
    delete_booking, booking_update, unauthorized,
    ProtectedBookingDeleteView, ProtectedBookingUpdateView
)
from django.urls import include, path
from django.conf import settings

# ----------------------drf-App----------------------urls

urlpatterns = [
    path('', fastfood_home, name='fastfood_home'),
    path('unauthorized/', unauthorized, name='unauthorized'),
    path('booking/', booking, name='booking'),
    path('bookings/', booking_list, name='bookings'),
    path('edit_booking/<str:user_id>/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('edit_booking/', include([
        path('<str:user_id>/<int:pk>/edit/', ProtectedBookingUpdateView.as_view(), name='booking_edit'),
        path('<str:user_id>/<int:pk>/delete/', ProtectedBookingDeleteView.as_view(), name='booking_delete'),
    ])),
    path('contactus/', contactus, name='contactus'),
    path('delete_booking/', delete_booking, name='delete_booking'),
    path('update_booking/', booking_update, name='update_booking'),
]
