from django.contrib import admin
from .models import MyData
# Register your models here.
class SensorData(admin.ModelAdmin):
    list_display = ['user','date_added']
    list_filter = ['user',  'date_added']
    # list_editable = ['code']
    search_fields = ['user',  'date_added']

admin.site.register(MyData,SensorData)