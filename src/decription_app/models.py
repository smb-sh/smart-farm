from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MyData(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    temp = models.CharField(max_length=200, blank=True)
    humi = models.CharField(max_length=200, blank=True)
    soilm = models.CharField(max_length=200, blank=True)
    rays = models.CharField(max_length=200, blank=True)
    rain = models.CharField(max_length=200, blank=True)
    date_added = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.sensor_data