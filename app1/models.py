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
		return self.rms_id+str(self.datetime)  #rms_id base view in db/admin panel


	class meta:
		verbose_name = 'pumpInstData'
		erbose_name_plural = 'pumpInstData'


	#def __init__(self, arg):
	#	super(ClassName, self).__init__()
	#	self.arg = arg

