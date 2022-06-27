from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from .serializers import DataSensor
from decription_app.models import MyData

class CreateMyView(CreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyData.objects.all()
    serializer_class = DataSensor
    # permission_classes = [permissions.IsAuthenticated]


