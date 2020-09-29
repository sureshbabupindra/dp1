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
from app1.models import md

from django.db.models import F
from django.db.models import Sum, Avg


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
            
            
               # start_date=datetime.strptime(request.GET["start"],"%Y-%m-%d")
                #end_date=datetime.strptime(request.GET["end"],"%Y-%m-%d")+timedelta(days=1)
                d = datetime.strptime(request.GET['TestDate'],"%Y-%m-%d").date()
                p = request.GET['ProjectName']
                c=datetime.now().date()
                #print(d)
                
                if d<c :
                    data = list(dd.objects.filter(Date__startswith=d, Project=p).values('Project','System_RID_No','Date','RunTime_Hrs','Water_Discharge_Lts','Pump_Consumption_KWH','Inverter_Input_KWH','Inverter_Output_KWH','Total_KWH_Generation','Gross_KWH'))
                    return JsonResponse({'Day Wise Data': data})
                else:
                    return HttpResponse('<h1>Inavalid Date Request<h1>')


            #else:
                #return HttpResponse('Error!')


def GetInvMonthData(request):

    d = datetime.strptime(request.GET['TestDate'],"%Y-%m-%d").date()
    p = request.GET['ProjectName']

    data = list(md.objects.filter(Date__startswith=d, Project=p).values('Project','System_RID_No','Date','RunTime_Hrs','Water_Discharge_Lts','Pump_Consumption_KWH','Inverter_Input_KWH','Inverter_Output_KWH','Total_KWH_Generation','Gross_KWH'))
    return JsonResponse({'Month Wise Data': data})


"""
def GetInvMonthData(request):
                     
               # start_date=datetime.strptime(request.GET["start"],"%Y-%m-%d")
                #end_date=datetime.strptime(request.GET["end"],"%Y-%m-%d")+timedelta(days=1)
                #d = datetime.strptime(request.GET['TestDate'],"%Y-%m-%d").date()
                #p = request.GET['ProjectName']
                #print(d)
                #data = dd.objects.filter(Date__range=((datetime.now())-timedelta(days=5), (datetime.now()))).aggregate(Sum('Gross_KWH'), Sum('Total_KWH_Generation'))
                #total = dd.objects.filter(Date__range=((datetime.now())-timedelta(days=5), (datetime.now()))).aggregate(Sum('Gross_KWH'))
                #data = list(dd.objects.filter(Date__range=((datetime.now())-timedelta(days=5), (datetime.now()))).values('Date', 'Gross_KWH'='total' ))
                #total = Sum(data)

                data = dd.objects.filter(Date__range=((datetime.now())-timedelta(days=7), (datetime.now())+timedelta(days=1))).order_by('System_RID_No')
                data1 = dd.objects.filter(Date__range=((datetime.now())-timedelta(days=7), (datetime.now())))
                a = dd.objects.filter(Date__range=((datetime.now())-timedelta(days=7), (datetime.now())++timedelta(days=1))).aggregate(Sum('Gross_KWH')).get('Gross_KWH__sum')

                MonthWiseData = []
                for x in data:
                    MonthWiseData.append({

                        "System_RID_No": x.System_RID_No,
                        "Date": x.Date,
                        "Gross_KWH": a,
                        
                        #"Total_KWH_Generation": x.filter(Date__range=((datetime.now())-timedelta(days=5), (datetime.now()))).aggregate(Sum('Total_KWH_Generation'))
                         
                    })

                


                    #context={'Month Wise Data': MonthWiseData}
                
                return JsonResponse({'Month Wise Data': MonthWiseData})

  """         



















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
