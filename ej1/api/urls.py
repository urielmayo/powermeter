from django.urls import path
from api import views

urlpatterns = [
    path('electricmeters/', view=views.ElectricMeterListView.as_view()),
    path('electricmeters/<uuid:pk>', view=views.ElectricMeterDetailView.as_view()),
    path('electricmeters/<uuid:uuid>/min/', view=views.ElectricMeterDetailMinView.as_view()),
    path('electricmeters/<uuid:uuid>/max/', view=views.ElectricMeterDetailMaxView.as_view()),
    path('electricmeters/<uuid:uuid>/total/', view=views.ElectricMeterDetailTotalView.as_view()),
    path('electricmeters/<uuid:uuid>/avg/', view=views.ElectricMeterDetailAvgView.as_view()),

    path('electricmeasures/', view=views.ElectricMeasureListView.as_view())
]