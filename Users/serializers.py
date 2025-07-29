from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """ This is what is returned as JSON 
    - This is dependent on the viewsOD
    """
    class Meta:
        model = User
        # The field to expose as  JSON
        fields = ['id', 'username', 'email', 'password']

        # ensure that a password is write-only and not returned in an API response
        extra_kwargs = {'password': {'write_only': True}}


