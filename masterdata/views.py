from django.shortcuts import render
from django.http import HttpResponse
from masterdata.models import Movie, Profile, MovieFeedback

# Create your views here.


def index(request):
    movie_obj = Movie.objects.all()
    profile_obj = Profile.objects.all()
    moviefeed_obj = MovieFeedback.objects.all()
    return render(request, 'index.html', locals())
    