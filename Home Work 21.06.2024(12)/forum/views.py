from django.http import HttpResponse
from django.shortcuts import render

def forum_home(request):
    return HttpResponse("ЭТО ФОРУМ ТУТ БУДЕМ ОБЩАТЬСЯ!")

def thread_detail(request, id):
    return HttpResponse(f"Details of thread with ID: {id}")

def user_profile(request, username):
    return HttpResponse(f"Profile of user: {username}")
