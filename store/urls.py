"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from api.models import ProductsDAO
from django.contrib import admin
from . import views
from . import settings

product_DAO = ProductsDAO()

handler400 = 'store.views.handler400'
handler403 = 'store.views.handler403'
handler404 = 'store.views.handler404'
handler500 = 'store.views.handler500'

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('api/', include(product_DAO.urls)),
]

# Show error views in debug mode
if settings.DEBUG:
    urlpatterns += [
        path('400/', views.handler400),
        path('403/', views.handler403),
        path('404/', views.handler404),
        path('500/', views.handler500),
    ]
