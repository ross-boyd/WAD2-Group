from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from bestboy.forms import RatingForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


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
            User = get_user_model()
            dog = form.save(commit=False)
            print(dog.owner.last_voted_id)
            dog.name = "LEO"
            dog.dog_id = "1000"
            dog.owner = User.objects.get(username="SUPERUSER")
            dog.rating = request.POST["slider_value"]
            dog.save()

    return render(request, 'vote.html')
