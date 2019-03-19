from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from bestboy.forms import RatingForm, UploadForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from bestboy.models import Dog
import re


def index(request):
    doggies = Dog.objects.all().order_by('-average')[:10]
    dog = []
    found = []
    for i in range(10):
        dog.append(str(doggies[i].picture))
        m = re.search('static/(.+?)$', dog[i])
        found.append(m.group(1))

    context = {'dog_id0': str(found[0]),
               'dog_id1': str(found[1]),
               'dog_id2': str(found[2]),
               'dog_id3': str(found[3]),
               'dog_id4': str(found[4]),
               'dog_id5': str(found[5]),
               'dog_id6': str(found[6]),
               'dog_id7': str(found[7]),
               'dog_id8': str(found[8]),
               'dog_id9': str(found[9]),
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
            
            dog = Dog.objects.get_or_create(dog_id=current_user.last_voted_id)[0]
            
            dog.rating += float(request.POST["slider_value"])
            dog.votes += 1

            dog.average = float(dog.rating) / dog.votes
            dog.save()

            current_user.last_voted_id += 1
            current_user.save()

    next_Dog = current_user.last_voted_id

    return render(request, 'vote.html', {"output": {id: str(next_Dog)}})


@login_required
def upload(request):
    User = get_user_model()
    current_user = User.objects.get(username=request.user)
    if request.method == "POST":
        print(request.POST)
        last_dog = Dog.objects.latest('dog_id')
        # Submits new dog when button is pressed
        dog = Dog.objects.get_or_create(dog_id=last_dog.dog_id+1,
                                        owner=current_user)[0]
        dog.name = request.POST['name']
        dog.picture = request.FILES['image']
        dog.save()

    return render(request, 'upload.html')


def profile(request, username):
    print(username)
    User = get_user_model()
    user = User.objects.get(username=username)
    print("HI")
    return render(request, 'profile.html', {'profile_user': user})
