from rest_framework import serializers
from .models import Trip
from Users.serializers import UserSerializer
from Routes.serializers import StopSerializer


class TripsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Trip
        # expose all fields for now
        fields = '__all__'

        # these fields are read-only during creation

        read_only_fields = ['passenger', 'fare']

class ConductorTripSerializer(serializers.ModelSerializer):
    """
    This is what the conductor will see.
    - They will see full details of passenger and dropoff location
    """

    passenger = UserSerializer(read_only=True)
    # Corrected field name below
    drop_off_location = StopSerializer(read_only=True)

    class Meta:
        # Corrected 'models' to 'model'
        model = Trip
        fields = [
            'id',
            'seat_number',
            'payment_status',
            'passenger',
            # Corrected field name below
            'drop_off_location'
        ]


