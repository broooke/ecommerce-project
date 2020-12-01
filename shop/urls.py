from django.urls import path
from .views import home, product

urlpatterns = [
    path('', home, name='home'),
    path('<slug:category_slug>', home, name = 'products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', product, name='products_detail'),
]