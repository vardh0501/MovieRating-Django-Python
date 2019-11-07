from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from masterdata.models import Movie, Profile, MovieFeedback
from django.contrib.auth import authenticate

# Create your views here.


def index(request):
    #import ipdb;ipdb.set_trace()
    movie_obj = Movie.objects.all()
    profile_obj = Profile.objects.all()
    moviefeed_obj = MovieFeedback.objects.all()
    return render(request, 'index.html', locals())
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', locals())
    else:
        #import ipdb;ipdb.set_trace()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponseRedirect("/home")
        else:
            message = "failure"
        return render(request, 'login.html', locals())

        #return HttpResponse(username+password)