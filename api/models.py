from django.db import models
from tastypie.resources import ModelResource
from products.models import Product

# Create your models here.


class ProductsDAO(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'products'
        excludes = ['date_created', 'entry_date']
