from django.urls import path, re_path
from .views import (
    index, by_rubric, BbCreateView, get_comments, post_comments, delete_comment, betting_view, 
    simple_html_response, redirect_to_index, display_query_params, display_post_params, 
    task_list, add_task, update_and_delete_tasks_view, task_detail, update_task, delete_task, 
    select_columns_view, exclude_tasks_view, tasks_created_on, tasks_by_priority, completed_tasks, 
    incomplete_tasks, search_tasks, export_tasks_csv, import_tasks_csv, tasks_by_tag
)

urlpatterns = [
    path('', index, name="index"),  
    path('add/', BbCreateView.as_view(), name='add'),  
    path('<int:rubric_id>/', by_rubric, name="by_rubric"), 

    path('comments/', get_comments, name='get_comments'), 
    path('comments/add/', post_comments, name='post_comments'), 
    path('comments/delete/<int:sms_id>/', delete_comment, name='delete_comment'),  

    path('betting/', betting_view, name='betting'),  
    path('redirect/', redirect_to_index, name='redirect_to_index'), 
    path('simple_html/', simple_html_response, name='simple_html'), 
    path('GET/', display_query_params, name='display_query_params'), 
    path('POST/', display_post_params, name='display_post_params'), 

    path('tasks/', task_list, name='task_list'),  
    path('add-task/', add_task, name='add_task'),  
    path('update-tasks/', update_and_delete_tasks_view, name='update_tasks'), 

    re_path(r'^tasks/(?P<task_id>\d+)/$', task_detail, name='task_detail'), 
    re_path(r'^tasks/update/(?P<task_id>\d+)/$', update_task, name='update_task'), 
    re_path(r'^tasks/delete/(?P<task_id>\d+)/$', delete_task, name='delete_task'),  

    path('select-columns/', select_columns_view, name='select_columns'),  
    path('exclude-tasks/', exclude_tasks_view, name='exclude_tasks'), 

    re_path(r'^tasks/created-on/(?P<date>\d{4}-\d{2}-\d{2})/$', tasks_created_on, name='tasks_created_on'),  
    re_path(r'^tasks/priority/(?P<level>\w+)/$', tasks_by_priority, name='tasks_by_priority'), 
    re_path(r'^tasks/search/(?P<keyword>\w+)/$', search_tasks, name='search_tasks'), 
    path('tasks/completed/', completed_tasks, name='completed_tasks'),  
    path('tasks/incomplete/', incomplete_tasks, name='incomplete_tasks'),  
    path('tasks/export/csv/', export_tasks_csv, name='export_tasks_csv'),  
    path('tasks/import/csv/', import_tasks_csv, name='import_tasks_csv'),
    re_path(r'^tasks/tagged/(?P<tag>\w+)/$', tasks_by_tag, name='tasks_by_tag'),
]

# index: / — Главная страница, отображает общий контент или список объявлений.
# add: /add/ — Добавление нового объявления через форму.
# by_rubric: /tasks/<rubric_id>/ — Отображает объявления по выбранной рубрике.
# get_comments: /comments/ — Просмотр всех комментариев.
# post_comments: /comments/add/ — Добавление нового комментария.
# delete_comment: /comments/delete/<int:sms_id>/ — Удаление комментария по его ID.
# betting: /betting/ — Пример страницы для ставок.
# redirect_to_index: /redirect/ — Перенаправление на главную страницу.
# simple_html_response: /simple_html/ — Отображение простого HTML ответа.
# display_query_params: /GET/ — Отображение GET параметров запроса.
# display_post_params: /POST/ — Отображение POST параметров запроса.
# task_list: /tasks/ — Список всех задач.
# add_task: /add-task/ — Добавление новой задачи.
# update_tasks: /update-tasks/ — Обновление и удаление задач.
# task_detail: /tasks/<task_id>/ — Отображение деталей задачи по ID.
# update_task: /tasks/update/<task_id>/ — Обновление задачи по ID.
# delete_task: /tasks/delete/<task_id>/ — Удаление задачи по ID.
# select_columns: /select-columns/ — Выбор определённых колонок из таблицы задач.
# exclude_tasks: /exclude-tasks/ — Исключение задач по определённым критериям.

# Фильтрация задач по дате создания: /tasks/created-on/<date>/
# Фильтрация задач по приоритету: /tasks/priority/<level>/
# Просмотр завершённых задач: /tasks/completed/
# Просмотр незавершённых задач: /tasks/incomplete/
# Поиск задач по ключевому слову: /tasks/search/<keyword>/
# Экспорт задач в CSV: /tasks/export/csv/
# Импорт задач из CSV: /tasks/import/csv/
# Отображение задач с определённым тегом: /tasks/tagged/<tag>/