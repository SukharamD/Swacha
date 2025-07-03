from django.contrib import admin
from django.urls import path, include
from myAuth import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'), 
    path('login/collector/', views.login_collector_view, name='login_collector'),
    path('register/collector/', views.register_collector_view, name='register_collector'),
    path('collector/dashboard/', views.collector_dashboard, name='dashboard_collector')

]
