from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet, ConductorManifestView

router = DefaultRouter()
router.register(r'', TripViewSet, basename='trip')

urlpatterns = [
        # This is the manifest endpoint
        path('manifest/', ConductorManifestView.as_view(), name='conductor-manifest'),
        path('', include(router.urls)),
        ]
