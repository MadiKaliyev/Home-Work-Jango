from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse, HttpResponsePermanentRedirect
from .models import Bb, Rubric, Comment
from .forms import BbForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from django.shortcuts import render, redirect
from .forms import TaskForm
import re

def index(request):
    bbs = Bb.objects.all().order_by('-published')
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = get_object_or_404(Rubric, pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

def get_comments(request):
    comments = Comment.objects.all()
    context = {'comments': comments}
    return render(request, 'bboard/comments.html', context)

@csrf_exempt
def post_comments(request):
    if request.method == "POST":
        text = request.POST.get('text')
        username = request.POST.get('username')
        user = None
        if username:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return render(request, 'bboard/comments.html', {'error': 'User does not exist', 'comments': Comment.objects.all()})

        new_comment = Comment.objects.create(text=text, user=user)
        return redirect('get_comments')

def betting_view(request):
    return render(request, 'bboard/betting.html')

def delete_comment(request, sms_id):
    comment = get_object_or_404(Comment, id=sms_id)
    comment.delete()
    return redirect('get_comments')

from django.http import HttpResponse

def simple_html_response(request):
    html_content = """
        <h1>HELLO!</h1>
    """
    return HttpResponse(html_content, content_type='text/html')

def redirect_to_index(request):
    index_url = reverse('index')  
    return HttpResponsePermanentRedirect(index_url)


def display_query_params(request):
    params = request.GET
    response_text = "It`s zapros GET\n"
    for key, value in params.items():
        response_text += f"{key}: {value}\n"
    return HttpResponse(response_text, content_type='text/plain')

def display_post_params(request):
    if request.method == 'POST':
        params = request.POST
        response_text = "HI it`s zapros(POST):\n"
        for key, value in params.items():
            response_text += f"{key}: {value}\n"
    else:
        response_text = "otpravte POST-zapros."
    return HttpResponse(response_text, content_type='text/plain')


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'bboard/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        Task.objects.create(description=description)
        return redirect('task_list')
    return render(request, 'bboard/add_task.html')

def update_and_delete_tasks_view(request):
    tasks = Task.objects.all()
    for task in tasks:
        task.description = f"{task.description} (ID: {task.id})"
        task.save()

    tasks = Task.objects.all()
    for task in tasks:
        if int(task.id) % 2 == 1:  
            task.delete()

    return redirect('task_list')

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'bboard/task_detail.html', {'task': task})

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.description = request.POST.get('description')
        task.save()
        return redirect('task_detail', task_id=task_id)
    return render(request, 'bboard/update_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def select_columns_view(request):
    selected_columns = Task.objects.values('description', 'deadline')
    return render(request, 'bboard/selected_columns.html', {'tasks': selected_columns})

def exclude_tasks_view(request):
    excluded_tasks = Task.objects.exclude(description__icontains='ЗАПИСЬ')
    return render(request, 'bboard/excluded_tasks.html', {'tasks': excluded_tasks})

def tasks_created_on(request, date):
    tasks = Task.objects.filter(created_on=date)
    return render(request, 'tasks_by_date.html', {'tasks': tasks})

def tasks_by_priority(request, level):
    tasks = Task.objects.filter(priority=level)
    return render(request, 'tasks_by_priority.html', {'tasks': tasks})

def search_tasks(request, keyword):
    tasks = Task.objects.filter(description__icontains=keyword)
    return render(request, 'search_tasks.html', {'tasks': tasks})

def completed_tasks(request):
    tasks = Task.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'tasks': tasks})

def incomplete_tasks(request):
    tasks = Task.objects.filter(is_completed=False)
    return render(request, 'incomplete_tasks.html', {'tasks': tasks})

def export_tasks_csv(request):
    pass

def import_tasks_csv(request):
    pass

def tasks_by_tag(request, tag):
    tasks = Task.objects.filter(tags__name=tag)
    return render(request, 'tasks_by_tag.html', {'tasks': tasks})

def select_columns_view(request):
    selected_columns = Task.objects.values('description', 'deadline')
    return render(request, 'selected_columns.html', {'tasks': selected_columns})

def exclude_tasks_view(request):
    excluded_tasks = Task.objects.exclude(description__icontains='ЗАПИСЬ')
    return render(request, 'excluded_tasks.html', {'tasks': excluded_tasks})