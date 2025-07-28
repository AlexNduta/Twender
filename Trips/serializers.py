from rest_framework import serializers
from .models import Trip

class TripsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Trip
        # expose all fields for now
        fields = '__all__'
