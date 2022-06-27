from decription_app.models import MyData
from rest_framework import serializers


class DataSensor(serializers.ModelSerializer):
    class Meta:
        model = MyData
        # fields = "__all__"
        exclude = ("date_added",)