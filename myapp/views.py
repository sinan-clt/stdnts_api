from django.shortcuts import render
from . models import *
from myapp.serilaizers import stdnts
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def studnts(request,id=0):
    if request.method=='GET':
        studnt_datas=students.objects.all()
        serializer_data=stdnts(studnt_datas, many='True')
        return JsonResponse(serializer_data.data, safe=False)

    elif request.method=='POST':
        userdata=JSONParser().parse(request)
        serlzerdata=stdnts(data=userdata)
        if serlzerdata.is_valid():
            serlzerdata.save()
            return JsonResponse('Data inserted succesfully', safe=False)
        return JsonResponse('An error occured', safe=False)

    elif request.method=='DELETE':
        deldatae=students.objects.get(id=id)
        deldatae.delete()
        return JsonResponse('data deleted' ,safe=False)
        
    elif request.method=='PUT':
        userdata=JSONParser().parse(request)
        user=students.objects.get(id=userdata['id'])
        serializerdata=stdnts(user,userdata)
        if serializerdata.is_valid():
            serializerdata.save()
            return JsonResponse('Data updated succesfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)