from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home.html')


# @login_required
# disabled for testing
def vote(request):
    return render(request, 'vote.html')
