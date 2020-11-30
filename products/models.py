from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db import models

# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to='img/')
    entry_date = models.DateField()
    stock = models.IntegerField()
    price = models.FloatField()
    # description = models.CharField(max_length=2000, null=True)
    description = RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
