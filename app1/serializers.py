
"""
from rest_framework import serializers

from .models import pumpInstData

class pumpInstDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pumpInstData
        fields = ('rms_id', 'datetime', 'flow_lph', 'power_kwh', 'voltage_pump', 'current_pump')
"""