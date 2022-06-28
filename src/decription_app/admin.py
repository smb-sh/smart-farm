from django.contrib import admin
from .models import MyData
# Register your models here.
class SensorData(admin.ModelAdmin):
    list_display = ['user','temp','humi','soilm','rays','rain','date_added']
    list_filter = ['user','temp','humi','soilm','rays','rain','date_added']
    # list_editable = ['code']
    search_fields = ['user','temp','humi','soilm','rays','rain','date_added']

admin.site.register(MyData,SensorData)