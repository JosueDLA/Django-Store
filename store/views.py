from django.template import RequestContext
from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def handler400(request, exception=None):
    return render(request, 'main/400.html', status=400)


def handler403(request, exception=None):
    return render(request, 'main/403.html', status=403)


def handler404(request, exception=None):
    return render(request, 'main/404.html', status=404)


def handler500(request, exception=None):
    return render(request, 'main/500.html', status=500)
