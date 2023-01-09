from django.contrib import admin

from api.models import ElectricMeter, ElectricMeasure
# Register your models here.
@admin.register(ElectricMeter)
class ElectricMeterAdmin(admin.ModelAdmin):
    '''Admin View for ElectricMeter'''

@admin.register(ElectricMeasure)
class ElectricMeasureAdmin(admin.ModelAdmin):
    '''Admin View for ElectricMeter'''