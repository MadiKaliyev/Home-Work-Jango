from django.http import HttpResponse
from django.shortcuts import render

def todo_list(request):
    return render(request, 'todo/todo_list.html')  # Отображение шаблона списка задач

def task_detail(request, id):
    return HttpResponse(f"Детали задания {id}")  # Отображение деталей задачи

def task_add(request):
    return HttpResponse("Добавь задание")  # Страница добавления задачи

def task_edit(request, id):
    return HttpResponse(f"Исправь задание {id}")  # Страница редактирования задачи

def task_delete(request, id):
    return HttpResponse(f"Удали задание {id}")  # Страница удаления задачи

def completed_tasks(request):
    return HttpResponse("Просмотр завершенных задач")  # Страница завершенных задач
