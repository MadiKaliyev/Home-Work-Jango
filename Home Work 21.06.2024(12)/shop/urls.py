from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_home, name='shop_home'),  # Исправлено на shop_home
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('category/<str:slug>/', views.category_products, name='category_products'),
]
