from django.contrib.auth.models import AbstractUser 
from django.db import models

class User(AbstractUser):
    # Determine if our user is a conductor
    is_conductor = models.BooleanField(default=False)
