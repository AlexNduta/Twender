from django.shortcuts import render
from rest_framework import viewsets
from .models import Route, Stop
from  .serializers import RouteSerializer, StopSerializer
# provide list of routes to the frontend


class RouteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing routes
    - we use ReadOnlyModelViewSet because the frontend will only read the routes
    and stops but not create them

    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class StopViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing stops
    """
    queryset = Stop.objects.all()
    serializer_class = StopSerializer



