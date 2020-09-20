from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/detail.html', {'product': product})
