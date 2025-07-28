from django.shortcuts import render
from rest_framework import viewsets
from .models import Trip
from .serializers import TripsSerialiser

class TripViewset(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripsSerialiser 

