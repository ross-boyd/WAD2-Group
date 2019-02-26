from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Rate Mah Dug</h1></br></br>Hello, world")
