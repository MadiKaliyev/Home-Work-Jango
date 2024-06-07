from django.urls import path
from . import views

urlpatterns = [
    path('', views.kiosk_home, name='kiosk_home'),  
    path('list/', views.kiosk_list, name='kiosk_list'), 
]
