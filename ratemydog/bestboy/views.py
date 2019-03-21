from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from bestboy.models import Dog, Rating
from bestboy.forms import RatingForm, UploadForm
from django.shortcuts import render_to_response
import re


def index(request):
    doggies = Dog.objects.all().order_by('-average')[:10]
    print(doggies)
    found = []
    context = {}
    for i in range(10):
        m = re.search('static/(.+?)$', str(doggies[i].picture))
        found.append(m.group(1))

        context["dog_id" + str(i)] = str(found[i])

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
            dog = Dog.objects.get(dog_id=current_user.last_voted_id + 1)
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
        doggies = Dog.objects.exclude(owner=current_user)
        vote = False
        for dog in doggies:
            if Rating.objects.all().filter(dog=dog, user=current_user).count() == 0:
                vote = True
                break
        if doggies.count() == 0 or vote is False:

                response = render_to_response("nodog.html")
                return response

        m = re.search('static/(.+?)$',
                      str(doggies[current_user.last_voted_id].picture))
        img = {'dogID': m.group(1)}

        dog = Dog.objects.get(dog_id=current_user.last_voted_id + 1)

        dogName = {'dogName': dog.name}
        ownerName = {'ownerName': dog.owner}
        comments = Rating.objects.all().filter(dog=dog).exclude(text="")
        commentsDict = {}
        for comment in comments:
            commentsDict[comment.user] = comment.text

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
            dog.picture = request.FILES['picture']
            dog.save()

            return redirect('/upload/')
    else:
        form = UploadForm()

    return render(request, 'upload.html', {'form': form})


def profile(request, username):
    User = get_user_model()

    user = User.objects.get(username=username)
    current_user = User.objects.get(username=username)

    dog_owner = Dog.objects.all().filter(owner=user).order_by('-average')[:10]
    voted_dogs = Dog.objects.all().filter(dog_id__lte=current_user.last_voted_id).order_by('-average')[:10]
    print(voted_dogs)
    display_dogs = []
    found = []
    found2 = []
    top_context = {}
    favourite_context = {}
    counter = 0

    for i in range(len(voted_dogs)):
        m = re.search('static/(.+?)$', str(voted_dogs[i].picture))
        found2.append(m.group(1))
        favourite_context["dog_id" + str(i)] = str(found2[i])

    for i in range(len(dog_owner)):
        m = re.search('static/(.+?)$', str(dog_owner[i].picture))
        found.append(m.group(1))
        top_context["dog_id" + str(i)] = str(found[i])

    return render(request, 'profile.html',
                  {'profile_user': user, 'output': top_context, "output2": favourite_context})


@login_required
def dogprofile(request, dogid):
    dog = Dog.objects.get(dog_id=dogid)
    comments = Rating.objects.all().filter(dog=dogid)
    commentsDict = {}
    for comment in comments:
        commentsDict[comment.user] = comment.text
    dogName = {'dogName': dog.name}
    ownerName = {'ownerName': dog.owner}
    comments = Rating.objects.all().filter(dog=dog).exclude(text='')
    commentsDict = {}
    m = re.search('static/(.+?)$',
                  str(dog.picture))
    img = {'dogID': m.group(1)}

    for comment in comments:
        commentsDict[comment.user] = comment.text

    return render(request, 'dogprofile.html',
                  {"dogInfo": dogName, "outputImg": img,
                   "ownerInfo": ownerName, "comments": commentsDict, })
