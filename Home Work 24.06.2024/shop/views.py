from django.http import HttpResponse
from django.shortcuts import render

def shop_home(request):
    return HttpResponse("Welcome to the Shop Home!")

def product_detail(request, id):
    return HttpResponse(f"Details of product with ID: {id}")

def category_products(request, slug):
    return HttpResponse(f"Products in category: {slug}")
