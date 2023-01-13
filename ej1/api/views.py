from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models import ElectricMeasure, ElectricMeter
from api.serializers import ElectricMeterSerializer, ElectricMeasureSerializer

# Create your views here.
class ElectricMeasureViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):

    serializer_class = ElectricMeasureSerializer
    queryset = ElectricMeasure.objects.all()

class ElectricMeterViewSet(mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):

    queryset = ElectricMeter.objects.all()
    serializer_class = ElectricMeterSerializer

    @action(detail=True)
    def min(self, request, pk):
        em = get_object_or_404(ElectricMeter, pk=pk)
        min_measure = ElectricMeasure.objects.filter(
            electric_meter=em
        ).order_by('kwh').first()
        serializer = ElectricMeasureSerializer(min_measure)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True)
    def max(self, request, pk):
        em = get_object_or_404(ElectricMeter, pk=pk)
        max_measure = ElectricMeasure.objects.filter(
            electric_meter=em
        ).order_by('kwh').last()
        serializer = ElectricMeasureSerializer(max_measure)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True)
    def total(self, request, pk):
        em = get_object_or_404(ElectricMeter, pk=pk)
        em_measures = ElectricMeasure.objects.filter(electric_meter=em)
        total_kwh = sum([measure.kwh for measure in em_measures])
        data = {
            'electric_meter': pk,
            'total_kwh': total_kwh
        }
        return Response(data)

    @action(detail=True)
    def avg(self, request, pk):
        em = get_object_or_404(ElectricMeter, pk=pk)
        em_measures = ElectricMeasure.objects.filter(electric_meter=em)
        avg_kwh = sum([measure.kwh for measure in em_measures]) / len(em_measures)
        data = {
            'electric_meter': pk,
            'average_kwh': round(avg_kwh, 2)
        }
        return Response(data)