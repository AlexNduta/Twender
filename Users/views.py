from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from .serializers import UserSerializer 
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


class UserViewSet(viewsets.ModelViewSet):
    """
    - the default ModelViewSet is designed for simple
    CRUD operations
    - we use the create() for secure login  
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    # This methos is called when we make a post request to /api/users/
    def create(self, request, *args, **kwargs):
        """ A secuer way to handle password management
        - Override the default create() with our own custom method
        """
        # standard validation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # custom logic begins here
        # lets hash the password before saving
        password = make_password(serializer.validated_data['password']) # this creates a hash    

        serializer.save(password=password)

        # standard success response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
