from django.shortcuts import render, redirect

def home(request):
    return render(request, 'myapp/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        return redirect('home')
    return render(request, 'myapp/login.html')
