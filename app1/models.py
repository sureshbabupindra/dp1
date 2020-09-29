from django.db import models

# Create your models here.
class pumpInstData(models.Model):
	"""docstring for ClassName"""
	rms_id = models.CharField(max_length=50,null=True,blank=True)
	datetime = models.DateTimeField(null=True,blank=True)
	flow_lph = models.IntegerField(null=True,blank=True)
	power_kwh = models.FloatField(null=True,blank=True)
	voltage_pump = models.FloatField(null=True,blank=True)
	current_pump = models.FloatField(null=True,blank=True)


	def __str__(self):   
		return self.rms_id
		#return self.rms_id+str(self.datetime)  #rms_id base view in db/admin panel


class ind(models.Model):
	"""docstring for ClassName"""
	Site_Code = models.CharField(max_length=30,null=True,blank=True)#models.ForeignKey(pumpInstData,on_delete=models.CASCADE, null=True,blank=True) 
	Test_Date = models.DateTimeField(null=True,blank=True)
	Flow = models.FloatField(null=True,blank=True)
	Power = models.FloatField(null=True,blank=True)
	Voltage = models.FloatField(null=True,blank=True)
	Currents = models.FloatField(null=True,blank=True)
	Temperature = models.FloatField(null=True,blank=True)
	RPM = models.IntegerField(null=True,blank=True)
	ONStat = models.CharField(max_length=10,null=True,blank=True)
	RunStat = models.CharField(max_length=10,null=True,blank=True)
	IsAlert = models.IntegerField(null=True,blank=True)
	IsFault = models.IntegerField(null=True,blank=True)
	Panel1_Voltage = models.FloatField(null=True,blank=True)
	Panel1_Current = models.FloatField(null=True,blank=True)
	DC_Power = models.FloatField(null=True,blank=True)
	Grid_Frequency = models.FloatField(null=True,blank=True)
	U_Voltage = models.FloatField(null=True,blank=True)
	V_Voltage = models.FloatField(null=True,blank=True)
	W_Voltage = models.FloatField(null=True,blank=True)
	U_Current = models.FloatField(null=True,blank=True)
	V_Current = models.FloatField(null=True,blank=True)
	W_Current = models.FloatField(null=True,blank=True)
	Temperature1 = models.FloatField(null=True,blank=True)

	def __str__(self):   
		return self.Site_Code




class dd(models.Model):
	"""docstring for ClassName"""
	Project = models.CharField(max_length=50,null=True,blank=True)
	System_RID_No = models.CharField(max_length=30,null=True,blank=True)
	Date = models.DateTimeField(null=True,blank=True)
	RunTime_Hrs = models.FloatField(null=True,blank=True)
	Water_Discharge_Lts = models.FloatField(null=True,blank=True)
	Pump_Consumption_KWH = models.FloatField(null=True,blank=True)
	Inverter_Input_KWH = models.FloatField(null=True,blank=True)
	Inverter_Output_KWH = models.FloatField(null=True,blank=True)
	Total_KWH_Generation = models.FloatField(null=True,blank=True)
	Gross_KWH = models.FloatField(null=True,blank=True)


	def __str__(self):   
		return self.System_RID_No+  str(self.Date)


class md(models.Model):
	"""docstring for ClassName"""
	Project = models.CharField(max_length=50,null=True,blank=True)
	System_RID_No = models.CharField(max_length=30,null=True,blank=True)
	Date = models.DateTimeField(null=True,blank=True)
	RunTime_Hrs = models.FloatField(null=True,blank=True)
	Water_Discharge_Lts = models.FloatField(null=True,blank=True)
	Pump_Consumption_KWH = models.FloatField(null=True,blank=True)
	Inverter_Input_KWH = models.FloatField(null=True,blank=True)
	Inverter_Output_KWH = models.FloatField(null=True,blank=True)
	Total_KWH_Generation = models.FloatField(null=True,blank=True)
	Gross_KWH = models.FloatField(null=True,blank=True)


	def __str__(self):   
		return self.System_RID_No+  str(self.Date)



class meta:   #for admin database actions
	verbose_name = 'pumpInstData'
	erbose_name_plural = 'pumpInstData'

class meta:   #for admin database actions
	verbose_name = 'ind'
	erbose_name_plural = 'ind'

class meta:   #for admin database actions
	verbose_name = 'dd'
	erbose_name_plural = 'dd'

class meta:   #for admin database actions
	verbose_name = 'md'
	erbose_name_plural = 'md'
















	#def __init__(self, arg):
	#	super(ClassName, self).__init__()
	#	self.arg = arg

