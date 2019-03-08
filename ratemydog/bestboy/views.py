from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from bestboy.forms import RatingForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from bestboy.models import Dog


def index(request):
    dog = Dog.objects.all().order_by('-average')[:10]
    context = {'dog_id0': str(dog[0].dog_id),
               'dog_id1': str(dog[1].dog_id),
               'dog_id2': str(dog[2].dog_id),
               'dog_id3': str(dog[3].dog_id),
               'dog_id4': str(dog[4].dog_id),
               'dog_id5': str(dog[5].dog_id),
               'dog_id6': str(dog[6].dog_id),
               'dog_id7': str(dog[7].dog_id),
               'dog_id8': str(dog[8].dog_id),
               'dog_id9': str(dog[9].dog_id),
               }
    return render(request, 'home.html', {"output": context})


@login_required
def vote(request):
    User = get_user_model()
    current_user = User.objects.get(username=request.user)

    # Submits dog rating when button is pressed
    if request.method == "POST": 
        form = RatingForm(request.POST)
        if form.is_valid():
            owner = User.objects.get(username="SUPERUSER")
            dog = Dog.objects.get_or_create(dog_id=current_user.last_voted_id)[0]

            dog.rating += float(request.POST["slider_value"])
            dog.votes += 1

            dog.average = float(dog.rating) / dog.votes
            dog.save()

            current_user.last_voted_id += 1
            current_user.save()

    next_Dog = current_user.last_voted_id+1

    return render(request, 'vote.html', {"output": {id: str(next_Dog)}})
