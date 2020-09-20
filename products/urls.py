from django.urls import path
from . import views

# products/1/details
urlpatterns = [
    path('', views.index, name='products_index'),
    path('<int:product_id>', views.detail, name='products_detail')
]
