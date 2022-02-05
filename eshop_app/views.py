from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def eshop_app(request):
    return render(request, 'eshop_app/main_app.html')


def about(request):
    return HttpResponse('hi dani hello')


def my_slug(request, slug):
    return HttpResponse(slug)
