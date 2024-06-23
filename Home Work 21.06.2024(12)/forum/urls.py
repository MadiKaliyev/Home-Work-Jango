from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.forum_home, name='forum_home'),
    path('thread/<int:id>/', views.thread_detail, name='thread_detail'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
]
