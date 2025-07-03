from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('update-profile/', views.update_profile_view, name='update_profile')
]