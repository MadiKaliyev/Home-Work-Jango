from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simple_html/', views.simple_html_response, name='simple_html'),
    path('redirect/', views.redirect_to_index, name='redirect_to_index'),
]
