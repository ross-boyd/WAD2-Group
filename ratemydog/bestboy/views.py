from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from bestboy.models import Dog, Rating
from bestboy.forms import RatingForm, UploadForm
from django.shortcuts import render_to_response
from ratemydog import settings


def index(request):
    top10 = Dog.objects.all().order_by('-average')[:10]
    context = {}
    for i in range(10):
        context[str(top10[i].id)] = "/media/" + str(top10[i].picture)

    return render(request, 'home.html', {"output": context})


@login_required
def vote(request):
    User = get_user_model()
    found = []
    current_user = User.objects.get(username=request.user)
    # Submits dog rating when button is pressed
    if request.method == "POST":
        form = RatingForm(request.POST)
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
        if len(request.GET) != 0:
            doggies = Dog.objects.exclude(owner=current_user).filter(breed=request.GET['breedFilter'])
        else:
            doggies = Dog.objects.exclude(owner=current_user)
        print(len(doggies))
        vote = False
        for dog in doggies:
            print(dog.breed, dog.id)
            if Rating.objects.all().filter(dog=dog, user=current_user).count() == 0:
                vote = True
                break
        if doggies.count() == 0 or vote is False:
            response = render_to_response("nodog.html")
            return render(request, 'nodog.html')

        print(current_user.last_voted_id)
        if len(request.GET) != 0:
            dog = Dog.objects.filter(dog_id__gte=current_user.last_voted_id + 1, breed=request.GET['breedFilter'])[:1].get()
        else:
            dog = Dog.objects.get(dog_id=current_user.last_voted_id + 1)
        
        img = {"dogID": "/media/" + str(dog.picture)}
        dogName = {"dogName": dog.name}
        ownerName = {"ownerName": dog.owner}
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

            return render(request, "success.html")
    else:
        form = UploadForm()

    return render(request, 'upload.html', {'form': form})


def profile(request, username):
    User = get_user_model()
    current_user = User.objects.get(username=username)

    top_rated = Dog.objects.all().filter(owner=current_user).order_by('-average')
    top_context = {}
    for i in range(10):
        try:
            top_context[str(top_rated[i].id)] = "/media/"+str(top_rated[i].picture)
        except:
            break

    favourite = Dog.objects.all().filter(dog_id__lte=current_user.last_voted_id).order_by('-average')
    favourite_context = {}
    for i in range(10):
        try:
            top_context[str(favourite[i].id)] = "/media/"+str(favourite[i].picture)
        except:
            break

    return render(request, 'profile.html',
                  {'profile_user': current_user, 'output': top_context,
                   "output2": favourite_context})


def dogprofile(request, dogid):
    dog = Dog.objects.get(dog_id=dogid)
    img = {"dogID": "/media/" + str(dog.picture)}
    dogName = {'dogName': dog.name}
    ownerName = {'ownerName': dog.owner}
    score = {"dog.average": dog.average}
    comments = Rating.objects.all().filter(dog=dog).exclude(text='')
    commentsDict = {}
    for comment in comments:
        commentsDict[comment.user] = comment.text

    return render(request, 'dogprofile.html',
                  {"dogInfo": dogName, "outputImg": img,
                   "ownerInfo": ownerName, "comments": commentsDict,
                   "score": score})
