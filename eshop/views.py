from django.shortcuts import render, HttpResponse


def about(request):
    return HttpResponse('hi dani hello')
