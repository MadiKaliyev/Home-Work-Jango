from django.urls import path, re_path
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
    path('add-task/', views.add_task, name='add_task'), 
    path('update-tasks/', views.update_and_delete_tasks_view, name='update_tasks'),  
    re_path(r'^tasks/(?P<task_id>\d+)/$', views.task_detail, name='task_detail'),
    re_path(r'^tasks/update/(?P<task_id>\d+)/$', views.update_task, name='update_task'),
    re_path(r'^tasks/delete/(?P<task_id>\d+)/$', views.delete_task, name='delete_task'),
]
# task_list: Список всех задач.
# add_task: Добавление задач.
# update_delete_tasks: Обновление и удаление задач.
# task_detail: Отображение деталей задачи по ID.
# update_task: Обновление задачи по ID.
# delete_task: Удаление задачи по ID.