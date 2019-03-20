from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from bestboy.models import Dog, Rating
from bestboy.forms import RatingForm, UploadForm
import re


def index(request):
    doggies = Dog.objects.all().order_by('-average')[:10]
    found = []
    for i in range(10):
        m = re.search('static/(.+?)$', str(doggies[i].picture))
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
        print(request.POST)
        if form.is_valid():
            dog = Dog.objects.get(dog_id=current_user.last_voted_id+1)
            dog.score += float(request.POST["slider_value"])
            dog.votes += 1
            dog.average = dog.score / dog.votes
            dog.save()

            current_user.last_voted_id += 1
            current_user.save()

            rating = form.save(commit=False)
            rating.dog = dog
            rating.user = current_user
            rating.score = request.POST["slider_value"]
            rating.save()

        return redirect('/vote/')

    else:
        form = RatingForm()
        doggies = Dog.objects.all()
        m = re.search('static/(.+?)$',
                      str(doggies[current_user.last_voted_id].picture))
        img = {'dogID': m.group(1)}

        dog = Dog.objects.get(dog_id=current_user.last_voted_id+1)

        dogName = {'dogName': dog.name}
        ownerName = {'ownerName': dog.owner}
        commentsDict = {'user0': 'comment0', 'user1': 'comment1'}

        return render(request, 'vote.html',
                      {"outputImg": img, "dogInfo": dogName,
                       "ownerInfo": ownerName, "comments": commentsDict,
                       "form": form})


@login_required
def upload(request):
    User = get_user_model()
    current_user = User.objects.get(username=request.user)
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            dog = form.save(commit=False)
            last_dog = Dog.objects.latest('dog_id')
            dog.dog_id = last_dog.dog_id + 1
            dog.owner = current_user
            dog.name = request.POST['name']
            dog.picture = form.clean_picture()
            dog.save()

        return redirect('/upload/')

    else:
        form = UploadForm()
        return render(request, 'upload.html', {'form': form})


def profile(request, username):
    print(username)
    User = get_user_model()

    print(User)
    user = User.objects.get(username=username)
    owner_dogs = Dog.objects.all().filter(owner=user).order_by('-average')

    display_dogs = []
    found = []
    context1 = {}
    counter = 0
    print(owner_dogs)
    print(owner_dogs.count())

    # if the user has no dogs returns empty dictionary
    if owner_dogs.count() <= 0:
        return render(request, 'profile.html',
                      {'profile_user': user, 'output': context1})

    # if the user has less than 10 dogs return as many as it has
    elif owner_dogs.count() < 10:
        print('less than 10')
        for i in range(owner_dogs.count()):
            display_dogs.append(str(owner_dogs[i].picture))

            m = re.search('static/(.+?)$', display_dogs[i])
            # print(m)

            found.append(display_dogs[i])
            print(owner_dogs[i].average)

            context1['dog_id' + str(counter)] = str(found[counter])
            counter += 1

    # if the user has more than ten dogs
    else:
        for i in range(10):
            display_dogs.append(str(owner_dogs[i].picture))

            m = re.search('static/(.+?)$', display_dogs[i])
            found.append(m.group(1))

            print(owner_dogs[i].average)

            context1['dog_id' + str(counter)] = str(found[counter])
            counter += 1

    return render(request, 'profile.html',
                  {'profile_user': user, 'output': context1})

from django.shortcuts import render_to_response

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def handler500(request, exception, template_name="500.html"):
    response = render_to_response("500.html")
    response.status_code = 500
    return response