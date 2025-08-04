from django.urls import path
from .views import InitiatePaymentView

urlpatterns =[
        path('initiate/', InitiatePaymentView.as_view(), name='initiate-payment'),
        path('callback/', MpesaCallbackView.as_view(), name='mpesa_callback'),
# Create your models here.
    ]
