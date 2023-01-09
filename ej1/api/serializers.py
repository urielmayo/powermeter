from rest_framework import serializers

from api.models import ElectricMeter, ElectricMeasure

class ElectricMeterSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectricMeter
        fields = '__all__'

class ElectricMeasureSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElectricMeasure
        fields = '__all__'