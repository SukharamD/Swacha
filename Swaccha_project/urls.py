
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myAuth.urls')),
    path('profile/', include('profiles.urls')),
    path('booking/', include('booking.urls'))
]
