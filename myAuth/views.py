from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from django.db import IntegrityError
from booking.models import Booking 


def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User doesnt exist", extra_tags='login')
            return redirect('login')  # 👈 redirect, not render

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password", extra_tags='login')
            return redirect('login')
            
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password!= confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')

    return render(request, 'register.html')

def logout_view(request):
    from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    if request.user.is_authenticated:
        is_collector = hasattr(request.user, 'userprofile') and request.user.userprofile.is_collector
        logout(request)
        if is_collector:
            return redirect('login_collector')  # or 'login_collector'
        else:
            return redirect('home')  # or 'login_user'
    return redirect('home')


from profiles.models import UserProfile

def register_collector_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register_collector')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register_collector')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register_collector')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)

            # ✅ Update the existing profile created by signal
            user.userprofile.is_collector = True
            user.userprofile.save()

            messages.success(request, "Collector account created successfully.")
            return redirect('login_collector')

        except IntegrityError as e:
            messages.error(request, f"Something went wrong: {str(e)}")
            return redirect('register_collector')

    return render(request, 'register_collector.html')



def login_collector_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                if user.userprofile.is_collector:
                    login(request, user)
                    return redirect('dashboard_collector')
                else:
                    messages.error(request, "You are not registered as a collector.")
            except UserProfile.DoesNotExist:
                messages.error(request, "No profile found for this user.")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'login_collector.html')



@login_required(login_url='login_collector')
def collector_dashboard(request):
    if request.user.userprofile.is_collector:
        bookings = Booking.objects.filter(
            collector__isnull=True,
            status='pending',
            user__isnull=False  # 🚫 Avoid bookings with deleted users
        )
        print(bookings)
    else:
        bookings = []
        print("User is not collector")

    return render(request, 'dashboard_collector.html', {'pending_bookings': bookings})

