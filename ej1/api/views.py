from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import ElectricMeasure, ElectricMeter
from api.serializers import ElectricMeterSerializer, ElectricMeasureSerializer

# Create your views here.
class ElectricMeterListView(ListCreateAPIView):
    """ electric meters List endpoint"""
    http_method_names = ['get', 'post']
    serializer_class = ElectricMeterSerializer
    queryset = ElectricMeter.objects.all()

class ElectricMeterDetailView(RetrieveUpdateAPIView):
    """ electric meter detail endpoint"""
    http_method_names = ['get']
    serializer_class = ElectricMeterSerializer
    queryset = ElectricMeter.objects.all()

class ElectricMeterDetailMinView(APIView):
    """ electric meter minimum measure endpoint"""
    def get(self, request, uuid):
        em = get_object_or_404(ElectricMeter, pk=uuid)
        min_measure = ElectricMeasure.objects.filter(
            electric_meter=em
        ).order_by('kwh').first()
        serializer = ElectricMeasureSerializer(min_measure)
        return Response(serializer.data)

class ElectricMeterDetailMaxView(APIView):
    """ electric meter maximum measure endpoint"""
    def get(self, request, uuid):
        em = get_object_or_404(ElectricMeter, pk=uuid)
        max_measure = ElectricMeasure.objects.filter(
            electric_meter=em
        ).order_by('kwh').last()
        serializer = ElectricMeasureSerializer(max_measure)
        return Response(serializer.data)

class ElectricMeterDetailTotalView(APIView):
    """ electric meter total measure endpoint"""
    def get(self, request, uuid):
        em = get_object_or_404(ElectricMeter, pk=uuid)
        em_measures = ElectricMeasure.objects.filter(electric_meter=em)
        total_kwh = sum([measure.kwh for measure in em_measures])
        data = {
            'electric_meter': uuid,
            'total_kwh': total_kwh
        }
        return Response(data)

class ElectricMeterDetailAvgView(APIView):
    """ electric meter average measure endpoint"""
    def get(self, request, uuid):
        em = get_object_or_404(ElectricMeter, pk=uuid)
        em_measures = ElectricMeasure.objects.filter(electric_meter=em)
        avg_kwh = sum([measure.kwh for measure in em_measures]) / len(em_measures)
        data = {
            'electric_meter': uuid,
            'average_kwh': round(avg_kwh, 2)
        }
        return Response(data)


class ElectricMeasureListView(ListCreateAPIView):
    """ electric measure list endpoint """
    http_method_names = ['get', 'post']
    serializer_class = ElectricMeasureSerializer
    queryset = ElectricMeasure.objects.all()