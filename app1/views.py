from django.shortcuts import render
#1 from django.http import HttpResponse
from django.http import HttpResponse
import requests
import json


from datetime import datetime, timedelta

from django.db import models
#from django.core import serializers

from django import http
from django.http import JsonResponse

from app1.models import pumpInstData
from app1.models import ind
from app1.models import dd

from django.db.models import F

#from rest_framework import viewsets

#from .serializers import pumpInstDataSerializer



def home(request):
	#1 return HttpResponse('<h1>Blog-Home<h1>')
	return render(request, 'blog/home.html') #rot to blog folder in templates and then home.html


def about(request):
	#1 return HttpResponse('<h1>Blog-About<h1>')
	return render(request, 'blog/about.html')



def abc(request):
    data = list(pumpInstData.objects.values('rms_id','datetime','flow_lph','power_kwh','voltage_pump','current_pump'))
    data1 = list(pumpInstData.objects.values('power_kwh','voltage_pump','current_pump'))
    return JsonResponse({'data': data, 'data1': data1})
    
def InstData(request):

    xy = pumpInstData.objects.all()
    for z in xy:
        if z.rms_id=="A-1001":
           z.flow_lph=z.flow_lph
        z.save()          
      

def Inst(request):

            data = list(pumpInstData.objects.filter(datetime__range=((datetime.now())-timedelta(minutes=90), (datetime.now()))).values('datetime','rms_id'))
            return JsonResponse({'data': data})

def GetInstataneousData(request):
            SpdData = list(ind.objects.filter(Test_Date__range=((datetime.now())-timedelta(minutes=180), (datetime.now()))).values('Site_Code','Test_Date'))
            InverterData = list(ind.objects.filter(Test_Date__range=((datetime.now())-timedelta(minutes=90), (datetime.now()))).values('Site_Code','Test_Date'))
            return JsonResponse({'SpdData': SpdData, 'InverterData': InverterData})



def GetInvDaysData(request):
            data = list(dd.objects.all().values('Project','System_RID_No','Date','RunTime_Hrs','Water_Discharge_Lts','Pump_Consumption_KWH','Inverter_Input_KWH','Inverter_Output_KWH','Total_KWH_Generation','Gross_KWH'))
            return JsonResponse({'Day Wise Data': data})
           



















"""
def abc(request):
    url = 'http://127.0.0.1:8000/abc'  # replace with other python app url or ip
    request_data = {'pumpInstData': 'rms_id'}  # replace with data to be sent to other app
    response = requests.post(url, json=request_data)
    response_data = response.json()  # data returned by other app
    return http.JsonResponse(response_data)
"""


"""
def abc(request):
    try:
        abc = pumpInstData.objects.all()
        a = []
        for abc in abc:
            b={
            "id":abc.rms_id,
           # "name":client.first_name,
            #"location":StatesOfIndia.STATES[client.location] 
            }
            a.append(b)
        return JsonResponse({"a":a})
        #except Exception as e:
        #return JsonResponse({"error":str(e)})
"""


"""
def abc(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data) 
"""


"""
    def abc(request):
    	data = pumpInstData.objects.get(id=1)
    	#for x in data:
    		#if x.rms_id=="A-1001":

				   data = {
				        "voltage_pump":data.voltage_pump
				    }
			return JsonResponse(data)
"""
		
"""
	def abc(request):
	    data = serializers.serialize('json',pumpInstData.objects.values('rms_id','flow_lph','power_kwh','voltage_pump','current_pump'))
	    return HttpResponse(data, content_type='application/json')
"""

""" 
    def abc(request):
		data = serializers.serialize('json',pumpInstData.objects.values())
		return JsonResponse({'data':data})
"""



"""
def abc(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')
"""



"""
def abc(request):

	#data = pumpInstData.objects.values()

    data = pumpInstData.objects.values('rms_id')
        
    
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')
"""

#class HeroViewSet(viewsets.ModelViewSet):

"""
def abc(request):
    data = [pumpInstData.objects.values('rms_id', 'datetime', 'flow_lph','power_kwh','voltage_pump','current_pump')]
    #serializer_class = pumpInstDataSerializer
    return HttpResponse(data, content_type='application/json')
"""    
