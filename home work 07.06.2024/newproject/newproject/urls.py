from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка Django
    path('icecreamkiosk/', include('icecreamkiosk.urls')),  # URL для приложения icecreamkiosk
]
