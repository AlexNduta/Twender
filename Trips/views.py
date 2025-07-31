from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Trip
from .serializers import TripsSerialiser
from Routes.logic import calculate_fare

# create trips using a logged-in user

class TripViewset(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripsSerialiser
    permission_classes = [permissions.IsAuthenticated]

    # override the create method

    def perform_create(self, serializer):
        # calculate the fare based on pickup and dropof

        pickup_stop = serializer.validated_data['pickup_location']
        dropoff_stop = serializer.validated_data[drop_off_location]
        # call the calculate_fare() 
        fare = calculate_fare(pickup_stop, dropoff_stop)

        # automatically make the loggedin user the passanger
        # save the calculated fare
        serializer.save(passenger=self.request.user, fare=fare)
