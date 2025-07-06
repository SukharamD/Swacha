from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Booking(models.Model):
    GARBAGE_TYPE_CHOICES = [
        ('wet', 'Wet'),
        ('dry', 'Dry'),
    ]

    QUANTITY_CHOICES = [
        ('0-20kg', 'Small (0-20kg)'),
        ('20-40kg', 'Medium (20-40kg)'),
        ('40-100kg', 'Large (40-100kg)'),
    ]

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )


    TIME_SLOT_CHOICES = [
        (f"{i}:00 - {i+1}:00", f"{i}:00 - {i+1}:00") for i in range(5, 18)
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    collector = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_bookings')
    garbage_type = models.CharField(max_length=10, choices=GARBAGE_TYPE_CHOICES)
    dry_types = models.CharField(max_length=100, blank=True)  # Comma-separated string
    quantity = models.CharField(max_length=20, choices=QUANTITY_CHOICES)
    date = models.DateField(default=datetime.date.today)
    time_slot = models.CharField(max_length=20, choices=TIME_SLOT_CHOICES, default='09:00 - 10:00')
    address = models.TextField()
    booked_at = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.date} at {self.time_slot} -  {self.status}- {self.id}"
