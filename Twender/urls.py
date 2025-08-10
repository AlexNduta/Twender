"""
URL configuration for Twender project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# views import
from Users.views import UserViewSet
#from Trips.views import TripViewset
from Routes.views import RouteViewSet, StopViewSet
from  drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# simple JWT imports
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
        )

# create routers and register our viewsets with it
router = DefaultRouter()
router.register(r'users', UserViewSet)
#router.register(r'trips', TripViewset)
router.register(r'routes', RouteViewSet)
router.register(r'stops', StopViewSet)


api_urlpatterns = [
    # urls from the router
    path('', include(router.urls)),

    # urls for JWT authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_pair'),
 #   path('mpesa/', include('mpesa.urls'))
        ]

# main url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include(api_urlpatterns)), # all API urls will be under  /api/
#    path('api/payments/', include('Payments.urls'))
    path('api/trips/', include('Trips.urls')),
    
    # API documentation 
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # optional UI
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
