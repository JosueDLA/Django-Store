from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})


def detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'products/detail.html', {'product': product})
    except Product.DoesNotExist:
        raise Http404()
