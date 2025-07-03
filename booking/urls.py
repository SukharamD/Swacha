from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_garbage, name='bookings'),
    path('collector/dashboard/', views.collector_dashboard, name='collector_dashboard'),
    path('collector/accept/<int:booking_id>/', views.accept_booking, name='accept_booking'),
    path('collector/reject/<int:booking_id>/', views.reject_booking, name='reject_booking'),
]
