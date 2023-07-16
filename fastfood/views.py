from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


class BookingUpdateView(LoginRequiredMixin, UpdateView):
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


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    success_url = reverse_lazy('delete_booking')
    template_name = 'fastfood/booking_confirm_delete.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


def fastfood_home(request):
    return render(request, 'fastfood/fastfood_home.html')


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


def contactus(request):
    return render(request, 'fastfood/contactus.html')


def delete_booking(request):
    return render(request, 'fastfood/delete_booking.html')


def booking_update(request):
    return render(request, 'fastfood/booking_form.html')


def unauthorized(request):
    return render(request, 'fastfood/unauthorized.html')


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


def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {'bookings': bookings}
    return render(request, 'fastfood/booking_list.html', context)
