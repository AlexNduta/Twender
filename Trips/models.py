from django.db import models
from django.conf import settings
from Routes.models import Stop


class Trip(models.Model):
    """ This is a trip's which includes the pickup and dropoff location
    - price is calucated depending on route and drop-off location
    """

    STATUSES = [('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')]

    passenger = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    # pickup and dropoff points will depend on the routes
    pickup_location = models.ForeignKey(Stop, related_name='depatures',
                                        on_delete=models.SET_NULL, null=True)
    drop_off_location = models.ForeignKey(Stop, related_name='arrivals', on_delete=models.SET_NULL, null=True)
    
    fare = models.IntegerField()
    seat_number = models.IntegerField()
    payment_status = models.CharField(max_length=12, choices=STATUSES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Trip for {self.passenger} from {self.pickup_location}"
