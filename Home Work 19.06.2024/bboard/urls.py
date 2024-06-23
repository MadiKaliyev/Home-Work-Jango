from django.urls import path
from .views import index, by_rubric, BbCreateView, get_comments, post_comments, delete_comment, betting_view, simple_html_response, redirect_to_index, display_query_params, display_post_params
from . import views

urlpatterns = [
    path('', index, name="index"),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name="by_rubric"),
    path('comments/', get_comments, name='get_comments'),
    path('comments/add/', post_comments, name='post_comments'),
    path('comments/delete/<int:sms_id>/', delete_comment, name='delete_comment'),
    path('betting/', betting_view, name='betting'),
    path('redirect/', redirect_to_index, name='redirect_to_index'),
    path('simple_html/', views.simple_html_response, name='simple_html'),
    path('GET/', views.display_query_params, name='display_query_params'),
    path('POST/', views.display_post_params, name='display_post_params'),
    path('tasks/', views.task_list, name='task_list'),
    path('add-tasks/', views.add_tasks, name='add_tasks'),
    path('update-tasks/', views.update_and_delete_tasks, name='update_tasks'),
]
