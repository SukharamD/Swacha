
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from booking.models import Booking  
from django.shortcuts import render, redirect
from django.contrib import messages

def profile_view(request):
    profile = UserProfile.objects.get(user=request.user)

    # ✅ Add this line to fetch user-specific orders
    orders = Booking.objects.filter(user=request.user).order_by('-booked_at')

    return render(request, 'profile.html', {
        'profile': profile,
        'orders': orders,  # ✅ pass orders to template
    })

@login_required
def update_profile_view(request):
    if request.method == 'POST':
        user = request.user
        profile = user.profile  # or user.userprofile depending on your model

        # Update fields from form
        user.email = request.POST.get('email')
        user.save()

        profile.phone_number = request.POST.get('phone')
        profile.location = request.POST.get('location')
        profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('dashboard')  # redirect back to dashboard or profile section

    return redirect('dashboard')