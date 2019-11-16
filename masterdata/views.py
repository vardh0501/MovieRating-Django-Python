from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from masterdata.models import Movie, Profile, MovieFeedback
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import  JsonResponse
from django.apps import apps


# Create your views here.


def index(request):
    #import ipdb;ipdb.set_trace()
    movie_obj = Movie.objects.all()
    profile_obj = Profile.objects.all()
    moviefeed_obj = MovieFeedback.objects.all()
    return render(request, 'index.html', locals())
    
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', locals())
    else:
        #import ipdb;ipdb.set_trace()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            message = 'sucuess'
            return HttpResponseRedirect("/home")
        else:
            message = "failure"
#        obj_data = {'status':True ,"message":message}
#        return JsonResponse(obj_data)
        return render(request, 'login.html', locals())

@csrf_exempt
def sample(request):
    if request.method == 'GET':
        movie_obj = apps.get_model('masterdata','movie')
        profile_obj = apps.get_model('masterdata','profile')
        moviefeedback_obj = apps.get_model('masterdata','moviefeedback')
        obj_json = list(obj.values())
        obj_data = {'status':True ,"data":obj_json}
        return JsonResponse(obj_data)
    elif request.method == 'POST':
        return HttpResponse('POST')




def commonjson(model):
#     if model == 'movie':
#          obj = apps.get_model('masterdata','movie')

#     if model == 'profile':
#         obj = apps.get_model('masterdata','profile')

#     if model == 'moviefeedback':
#         obj = apps.get_model('masterdata','moviefeedback')
    #import ipdb;ipdb.set_trace()
    obj = apps.get_model('masterdata',model)
    obj_json = list(obj.objects.values())
    obj_data = {'status':True ,"data":obj_json}
    return obj_data



def profile(request,model):
    if request.method == 'GET':
        #obj = Profile.objects.all()
        #obj_json = list(obj.values())
        #obj_data = {'status':True ,"data":obj_json}
        obj_data = commonjson(model)
        return JsonResponse(obj_data)
    elif request.method == 'POST':
        return HttpResponse('POST')

def movie(request):
    if request.method == 'GET':
        obj = Movie.objects.all()
        obj_json = list(obj.values())
        obj_data = {'status':True ,"data":obj_json}
        obj_data = commonjson('movie')
        return JsonResponse(obj_data)
    elif request.method == 'POST':
        return HttpResponse('POST')


def moviefeedback(request):
    if request.method == 'GET':
        obj =  MovieFeedback.objects.all()
        obj_json = list(obj.values())
        obj_data = {'status':True ,"data":obj_json}
        obj_data = commonjson('moviefeedback')
        return JsonResponse(obj_data)
    elif request.method == 'POST':
        return HttpResponse('POST')
        
