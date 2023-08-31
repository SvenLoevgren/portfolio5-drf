from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking, MenuItem
from .forms import BookingForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookingSerializer, MenuItemUpdateSerializer, MenuItemCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView,
    ListAPIView, DestroyAPIView, UpdateAPIView
)
from .serializers import BookingSerializer, MenuItemSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.decorators import user_passes_test


# ------------------------------------------------------User settings for drf bookings


def user_is_owner(user, user_id):
    return str(user.id) == user_id

# ------------------------------------------------------Menu Views for REACT app

# ------------------react----------------------Menu Read


class MenuAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch menu items from the database
        menu_items = MenuItem.objects.all()

        # Serialize the menu items to JSON
        serializer = MenuItemSerializer(menu_items, many=True)

        # Return the serialized data as a JSON response
        return Response(serializer.data)

# ------------------react----------------------Menu Delete


class MenuItemDeleteView(DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

# ------------------react----------------------Menu Update


class MenuItemUpdateView(UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return MenuItemUpdateSerializer
        return self.serializer_class

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

# ------------------react----------------------Menu Create


class MenuItemCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        menu_items_data = request.data
        created_items = []

        for item_data in menu_items_data:
            serializer = MenuItemCreateSerializer(data=item_data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                created_items.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(created_items, status=status.HTTP_201_CREATED)

# ------------------------------------------------------Booking Views for drf App

# ---------------------drf---------------------Booking Create


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been confirmed, we will contact you via email!')
            return redirect('bookings')
    else:
        form = BookingForm()
    return render(request, 'fastfood/booking.html', {'form': form})

# ---------------------drf---------------------Booking Read


def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {'bookings': bookings}
    return render(request, 'fastfood/booking_list.html', context)

# ---------------------drf---------------------Booking Details


def edit_booking(request, user_id, booking_id):
    if request.user.is_authenticated and str(request.user.id) == user_id:
        booking = get_object_or_404(Booking, id=booking_id, user_id=user_id)
        context = {
            'booking_id': booking_id,
            'booking': booking,
            'user_id': user_id
        }
        return render(request, 'fastfood/edit_booking.html', context)
    else:
        # Handle unauthorized access if user tries to change URL in the web-browser
        return redirect('unauthorized')

# ---------------------drf---------------------Booking Delete


def delete_booking(request):
    return render(request, 'fastfood/delete_booking.html')


class ProtectedBookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    success_url = reverse_lazy('delete_booking')
    template_name = 'fastfood/booking_confirm_delete.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


protected_delete_view = user_passes_test(
    lambda u: user_is_owner(u, user_id), login_url='unauthorized')
(ProtectedBookingDeleteView.as_view())

# ---------------------drf---------------------Booking Update


class ProtectedBookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ['customer_name', 'email', 'phone_number', 'date', 'time', 'num_seats']
    success_url = reverse_lazy('bookings')
    template_name = 'fastfood/booking_form.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def form_invalid(self, form):
        messages.error(self.request, 'Phone number = +46-709999999; Date = yyyy-mm-dd; Time = hh:mm')
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Booking updated successfully!')
        return super().form_valid(form)


protected_update_view = user_passes_test(
    lambda u: user_is_owner(u, user_id), login_url='unauthorized')
(ProtectedBookingUpdateView.as_view())


def booking_update(request):
    return render(request, 'fastfood/booking_form.html')

# --------------------------------------------------Other drf app views


def fastfood_home(request):
    return render(request, 'fastfood/fastfood_home.html')


def contactus(request):
    return render(request, 'fastfood/contactus.html')


def unauthorized(request):
    return render(request, 'fastfood/unauthorized.html')
