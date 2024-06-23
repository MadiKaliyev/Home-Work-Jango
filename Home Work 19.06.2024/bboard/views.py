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
    context = {'tasks': tasks}
    return render(request, 'bboard/task_list.html', context)


def add_tasks(request):
    for i in range(20):
        Task.objects.create(description=f'ЗАПИСЬ {i+1}')
    return redirect('task_list')

def update_and_delete_tasks(request):
    tasks = Task.objects.all()
    for task in tasks:
        task.description = f"{task.description} ({task.id})"
        task.save()

    tasks = Task.objects.all()
    for task in tasks:
        if re.search(r'[13579]', task.description):
            task.delete()

    return redirect('task_list')