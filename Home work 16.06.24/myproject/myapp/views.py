from django.shortcuts import render
from .models import Product, Customer
from django.http import HttpResponse
from django.apps import apps

def products_view(request):
    products = Product.objects.all()
    total_price = Product.sum_prices()
    return render(request, 'myapp/products.html', {
        'products': products,
        'total_price': total_price
    })

def customers_view(request):
    customers = Customer.objects.all()
    total_age = Customer.sum_ages()
    return render(request, 'myapp/customers.html', {
        'customers': customers,
        'total_age': total_age
    })

def home(request):
    return render(request, 'myapp/home.html')

def list_view(request, model):
    Model = apps.get_model('myapp', model)
    objects = Model.objects.all()
    total_sum = Model.sum_prices() if model == 'Product' else Model.sum_ages()
    context = {
        'objects': objects,
        'total_sum': total_sum,
        'model_name': model
    }
    return render(request, 'myapp/list.html', context)