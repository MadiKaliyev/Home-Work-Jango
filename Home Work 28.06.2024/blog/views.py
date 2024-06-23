from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse

def index(request):
    return HttpResponse("<h1>Главная страница блога</h1>")

def simple_html_response(request):
    html_content = """
            <h1>Привет!</h1>
    """
    return HttpResponse(html_content, content_type='text/html')

def redirect_to_index(request):
    index_url = reverse('index')
    return HttpResponsePermanentRedirect(index_url)
