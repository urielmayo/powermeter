from django.db import models
from django.core.validators import MinValueValidator
import uuid
from datetime import datetime
# Create your models here.
class ElectricMeter(models.Model):
    """Model definition for ElectricMeter."""

    # I used id uuid as primary key, but it can also be a chrafield
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for ElectricMeter."""

        verbose_name = 'Electric Meter'
        verbose_name_plural = 'Electric Meters'

    def __str__(self):
        """Unicode representation of ElectricMeter."""
        return self.name

class ElectricMeasure(models.Model):
    """Model definition for ElectricMeasure."""

    electric_meter = models.ForeignKey(ElectricMeter, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    kwh = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    class Meta:
        """Meta definition for ElectricMeasure."""

        verbose_name = 'Electric Measure'
        verbose_name_plural = 'Electric Measures'

    def __str__(self):
        return f'{self.electric_meter} {self.date.strftime("%d/%m/%Y, %H:%M:%S")} KWH:{self.kwh}'