from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from bestboy.forms import RatingForm


def index(request):
    return render(request, 'home.html')


# @login_required
# disabled for testing

def vote(request):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            # Will add other field details when we have more dog information on 
            # the vote page
            dog = form.save(commit=False)
            dog.name = "LEO"
            dog.rating = request.POST["slider_value"]
            dog.save()

    return render(request, 'vote.html')
