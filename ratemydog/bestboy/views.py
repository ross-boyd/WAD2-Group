from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from bestboy.forms import RatingForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from bestboy.models import Dog


def index(request):
    return render(request, 'home.html')


@login_required
def vote(request):
        if request.method == "POST":
                form = RatingForm(request.POST)
                if form.is_valid():
                        # Will add other field details when we have more dog
                        # information on the vote page
                        User = get_user_model()
                        owner = User.objects.get(username="SUPERUSER")
                        dog = Dog.objects.get_or_create(owner=owner,
                                                        dog_id=1000)
                        print(dog)
                        if dog[1] is False:
                                dog[0].name = "LEO"
                                dog[0].dog_id = "1000"
                                dog[0].rating = request.POST["slider_value"]
                                dog[0].votes += 1
                        else:
                                dog[0].vote += 1
                        dog.save()

        return render(request, 'vote.html')
