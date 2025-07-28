from django.db import models
from django.conf import settings

class Trip(models.Model):
    STATUSES = [('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')]

    passenger = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=250)
    drop_off_location = models.CharField(max_length=250)
    fare = models.IntegerField()
    seat_number = models.IntegerField()
    payment_status = models.CharField(max_length=12, choices=STATUSES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Trip for {self.passenger} from {self.pickup_location}"
