from django.db import models
from django.db.models import DecimalField


class Place(models.Model):
    name = models.CharField(max_length=200)
    latitude = DecimalField(max_digits=9, decimal_places=6)
    longitude = DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
