from django.shortcuts import render
from rest_framework import viewsets
from .models import Trip
from .serializers import TripsSerialiser
from .logic import calculate_fare


class TripViewset(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripsSerialiser 

    # override the create method

    def perform_create(self, serializer):
        # calculate the fare based on pickup and dropoff
        fare = calculate_fare(
                serializer.validated_data['pickup_location'],
                serializer.validated_data['drop_off_location']
                )
        # automatically make the loggedin user the passanger
        # save the calculated fare
        serializer.save(passenger=self.request.user, fare=fare)
