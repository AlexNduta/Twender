from rest_framework import serializers
from .models import Route, Stop

class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ['id', 'name', 'order']


class RouteSerializer(serializers.ModelSerializer):
    # nest the stop serializer to show all stops of a route
    stops = StopSerializer(many=True, read_only=True)

    class Meta:
        model = Route
        # this is what will be returned as JSON
        fields = ['id', 'name', 'stops']
