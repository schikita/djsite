from django.shortcuts import HttpResponse
from django.shortcuts import render


def index(request):  # HTTPRequest
    return HttpResponse("Страница приложения опросника")


def categories(request):
    return HttpResponse("<h1>Опрос посетителя по болезни</h1>")
