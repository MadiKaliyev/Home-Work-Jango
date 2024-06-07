from django.http import HttpResponse

def kiosk_home(request):
    return HttpResponse("Welcome to the Ice Cream Kiosk!")

def kiosk_list(request):
    return HttpResponse("List of Ice Cream Kiosks")
