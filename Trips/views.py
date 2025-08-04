from rest_framework import viewsets, permissions
from .models import Trip
from .serializers import TripsSerialiser, ConductorTripSerializer
from Routes.logic import calculate_fare
from Users.permissions import IsConductor
from rest_framework.generics import ListAPIView

# create trips using a logged-in user

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripsSerialiser
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        """
        - the ai is to have any authenticated user create a trip
        - only conductor can update the status
        """
        if self.action in ['update', 'partial_update']:
            # only the conductor can update the trip
            permission_classes = [permissions.IsAuthenticated, IsConductor]
        else:
            # Any authenticated user can create a trip
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    # override the create method

    def perform_create(self, serializer):
        # calculate the fare based on pickup and dropof
        pickup_stop = serializer.validated_data['pickup_location']
        dropoff_stop = serializer.validated_data['drop_off_location']
        
        # call the calculate_fare() 
        fare = calculate_fare(pickup_stop, dropoff_stop)

        # automatically make the loggedin user the passanger
        # save the calculated fare
        serializer.save(passenger=self.request.user, fare=fare)

class ConductorManifestView(ListAPIView):
    """
    Provide a read-only list of all trips for conductors

    """
    queryset = Trip.objects.all()
    serializer_class = ConductorTripSerializer
    permission_classes = [permissions.IsAuthenticated, IsConductor]
