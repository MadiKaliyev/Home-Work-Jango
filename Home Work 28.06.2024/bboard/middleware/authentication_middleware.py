
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in ['/login/', '/register/']:
            return HttpResponseRedirect('/login/')

        response = self.get_response(request)
        return response
