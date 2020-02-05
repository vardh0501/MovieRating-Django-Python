from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from masterdata.models import SD_creation, MD_creation, Donor, Profile
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import  JsonResponse
from django.apps import apps

    
@csrf_exempt
def listdonor(request):
    if request.method == 'GET':
        obj = apps.get_model('masterdata','donor')
        obj_json = list(obj.objects.values())
        obj_data = {'status':True ,"data":obj_json}
        return JsonResponse(obj_data)
    elif request.method == 'POST':
        return HttpResponse('POST')

    
@csrf_exempt
def adddonor(request):
    if request.method == 'POST':

        #import ipdb;ipdb.set_trace()
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        amount = request.POST.get("amount")
        Donor.objects.create(first_name=first_name,last_name=last_name,amount=amount)
        obj_data = {"message":"sucuessfully added","status":True}
        return JsonResponse(obj_data)



def deletedonor(request,pk):
    obj = Donor.objects.get(pk=pk)



    #obj.d_name = dir_name
    obj.delete()


    obj_data = {"message":"sucuessfully deleted","status":True}
    return JsonResponse(obj_data)

def list_sd_creation(request):
    if request.method == 'GET':
        obj = apps.get_model('masterdata','SD_creation')
        obj_json = list(obj.objects.values())
        obj_data = {'status':True ,"data":obj_json}
        return JsonResponse(obj_data)
    elif request.method == 'POST':
        return HttpResponse('POST')

    
@csrf_exempt
def add_sd_creation(request):
    if request.method == 'POST':

        #import ipdb;ipdb.set_trace()
        name = request.POST.get("name")
        creation_name = request.POST.get("creation_name")
        SD_creation.objects.create(name=name,creation_name=creation_name)
        obj_data = {"message":"sucuessfully added","status":True}
        return JsonResponse(obj_data)

def delete_sd_creation(request,pk):
    obj = SD_creation.objects.get(pk=pk)



    #obj.d_name = dir_name
    obj.delete()


    obj_data = {"message":"sucuessfully deleted","status":True}
    return JsonResponse(obj_data)

def list_md_creation(request):
    if request.method == 'GET':
        obj = apps.get_model('masterdata','MD_creation')
        obj_json = list(obj.objects.values())
        obj_data = {'status':True ,"data":obj_json}
        return JsonResponse(obj_data)
    elif request.method == 'POST':
        return HttpResponse('POST')

    
@csrf_exempt
def add_md_creation(request):
    if request.method == 'POST':

        #import ipdb;ipdb.set_trace()
        name = request.POST.get("name")
        date_creation= request.POST.get("date_creation")
        MD_creation.objects.create(name=name,date_creation=date_creation)
        obj_data = {"message":"sucuessfully added","status":True}
        return JsonResponse(obj_data)

def delete_md_creation(request,pk):
    obj = MD_creation.objects.get(pk=pk)



    #obj.d_name = dir_name
    obj.delete()


    obj_data = {"message":"sucuessfully deleted","status":True}
    return JsonResponse(obj_data)



@csrf_exempt
def editdonor(request,pk):
    if request.method == 'GET':
        obj = Donor.objects.get(pk=pk)
        json_data = {"first_name":obj.first_name,"last_name":obj.last_name,"amount":obj.amount}
        obj_data = {"data":json_data,"status":True}
        return JsonResponse(obj_data)
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        amount= request.POST.get("amount")
        obj = Donor.objects.get(pk=pk)

        obj.first_name = first_name
        obj.last_name = last_name
        obj.amount = amount
        obj.save()
        obj_data = {"message":"sucuessfully Updated","status":True}
        return JsonResponse(obj_data)
        
@csrf_exempt
def edit_sd_creation(request,pk):
    if request.method == 'GET':
        obj = SD_creation.objects.get(pk=pk)
        json_data = {"name":obj.name,"creation_name":obj.creation_name}
        obj_data = {"data":json_data,"status":True}
        return JsonResponse(obj_data)
    if request.method == 'POST':
        name = request.POST.get("name")
        creation_name = request.POST.get("creation_name")
        obj = SD_creation.objects.get(pk=pk)

        obj.name = name
        obj.creation_name = creation_name
        obj.save()
        obj_data = {"message":"sucuessfully Updated","status":True}
        return JsonResponse(obj_data)
        
@csrf_exempt
def edit_md_creation(request,pk):
    if request.method == 'GET':
        obj = MD_creation.objects.get(pk=pk)
        json_data = {"name":obj.name,"date_creation":obj.date_creation}
        obj_data = {"data":json_data,"status":True}
        return JsonResponse(obj_data)
    if request.method == 'POST':
        name = request.POST.get("name")
        date_creation = request.POST.get("date_creation")
        obj = MD_creation.objects.get(pk=pk)

        obj.name = name
        obj.date_creation = date_creation
        obj.save()
        obj_data = {"message":"sucuessfully Updated","status":True}
        return JsonResponse(obj_data)
        
@csrf_exempt
def add_profile(request):
    if request.method == 'POST':

        #import ipdb;ipdb.set_trace()
        profile_name = request.POST.get("profile_name")
        book_id= request.POST.get("book_id")
        subject = request.POST.get("subject")
        Profile.objects.create(profile_name=profile_name,book_id=book_id,subject=subject)
        obj_data = {"message":"sucuessfully added","status":True}
        return JsonResponse(obj_data)

def edit_profile(request,pk):
    if request.method == 'GET':
        obj = Profile.objects.get(pk=pk)
        json_data = {"profile_name":obj.profile_name,"book_id":obj.book_id,"subject":obj.subject}
        obj_data = {"data":json_data,"status":True}
        return JsonResponse(obj_data)
    if request.method == 'POST':
        profile_name = request.POST.get("profile_name")
        book_id = request.POST.get("book_id")
        subject = request.POST.get("subject")

        obj = Profile.objects.get(pk=pk)

        obj.profile_name = profile_name
        obj.book_id = book_id
        obj.subject = subject
        obj.save()
        obj_data = {"message":"sucuessfully Updated","status":True}
        return JsonResponse(obj_data)

def delete_profile(request,pk):
    obj = Profile.objects.get(pk=pk)



    #obj.d_name = dir_name
    obj.delete()


    obj_data = {"message":"sucuessfully deleted","status":True}
    return JsonResponse(obj_data)



