from django.contrib import admin
from .views import fastfood_home, booking, contactus, booking_list, edit_booking, delete_booking, booking_update, unauthorized, BookingDeleteView, BookingUpdateView
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fastfood_home, name='fastfood_home'),
    path('accounts/', include('allauth.urls')),
    path('unauthorized/', unauthorized, name='unauthorized'),
    path('booking/', booking, name='booking'),
    path('bookings/', booking_list, name='bookings'),
    path('edit_booking/<str:user_id>/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('edit_booking/', include([
        path('<str:user_id>/<int:pk>/edit/', BookingUpdateView.as_view(), name='booking_edit'),
        path('<str:user_id>/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
    ])),
    path('contactus/', contactus, name='contactus'),
    path('delete_booking/', delete_booking, name='delete_booking'),
    path('update_booking/', booking_update, name='update_booking'),
]
