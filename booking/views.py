from django.shortcuts import render, redirect
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required(login_url='login')
def book_garbage(request):
    time_slots = [f"{i}:00 - {i+1}:00" for i in range(5, 18)]

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            dry_types = form.cleaned_data.get('dry_types')
            if dry_types:
                booking.dry_types = ', '.join(dry_types)
            booking.save()

            messages.success(request, "Booking Successful!")
            return redirect('bookings')

    else:
        form = BookingForm()

    return render(request, 'bookings.html', {'form': form, 'time_slots': time_slots})


@login_required
def collector_dashboard(request):
    collector = request.user

    pending_bookings = Booking.objects.filter(
        Q(status='pending', collector=None) |
        Q(collector=collector)
    ).order_by('-booked_at')

    return render(request, 'collector_dashboard.html', {'pending_bookings': pending_bookings})

@login_required
def accept_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.status == 'pending':
        booking.status = 'accepted'
        booking.collector = request.user
        booking.save()
    return redirect('collector_dashboard')

@login_required
def reject_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.status == 'pending':
        booking.status = 'rejected'
        booking.save()
    return redirect('collector_dashboard')

