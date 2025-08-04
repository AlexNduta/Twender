from django.db import models
from django.conf import settings
from Trips.models import Trip


class Payment(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)


    # these fields will be managed by the Daraja API callback
    is_succesful = models.BooleanField(default=False)
    mpesa_receipt_number = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_callback_urls(self):
        return reverse('mpesa_callback')

    def __str__(self):
        return f"payment of {self.amount} for Trip {self.trip.id}"
