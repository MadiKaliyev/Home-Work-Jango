from django.urls import re_path
from . import views

app_name = 'todo'  # Псевдоним приложения todo

urlpatterns = [
    re_path(r'^$', views.todo_list, name='todo_list'),  # Главная страница со списком задач
    re_path(r'^task/(?P<id>\d+)/$', views.task_detail, name='task_detail'),  # Детальная страница задачи
    re_path(r'^task/add/$', views.task_add, name='task_add'),  # Страница добавления новой задачи
    re_path(r'^task/(?P<id>\d+)/edit/$', views.task_edit, name='task_edit'),  # Страница редактирования задачи
    re_path(r'^task/(?P<id>\d+)/delete/$', views.task_delete, name='task_delete'),  # Страница удаления задачи
    re_path(r'^completed/$', views.completed_tasks, name='completed_tasks'),  # Страница завершенных задач
]
