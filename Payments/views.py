
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#from mpesa.models import MpesaExpress, MpesaResponse
from Trips.models import Trip
from .models import Payment
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django_daraja.mpesa.core import MpesaClient

# takes a trip_id and trigger an STK push using django-mpesa

class InitiatePaymentView(CreateAPIView):
    permission_classes= [IsAutheticated]

    def post(self, request, *args, **kwargs):
        trip_id = request.data.get('trip-id')
        phone_number = request.data.get('phone_number')


        try:
            trip = Trip.objects.get(id=trip_id, passenger=request.user)
        except Trip.DoesnotExist:
            return Response({"error": "Trip not found."}, status=404.HTTP_404_NOT_FOUND)

        # create an instance of the mpesa client
        cl = MpesaClient()

        # create a payment record


        """payment = Payment.objects.create(
                trip=trip,
                amount=trip.fare,
                phone_number=phone_number
                )
            """
        # initiate STK push
        response = cl.stk_push(
                phone_number=phone_number,
                amount=int(trip.fare),
                account_reference="Twender",
                transaction_desc=f"Payment for trip{trip.id}",
                callback_url=payment.get_callback_url()
                )
        return Response(response)

@method_decorator(csrf_exempt, name='dispatch')
class MpesaCallbackView(CreateAPIView):
    queryset = Payment.objects.all()

    def create(self, request, *args, **kwargs):
        mpesa_response = MpesaResponse(request.data)

        if mpesa_response.is_successful():
            print("successful M-Pesa callback received.")

        else:
            print("Failed M-Pesa callback received")

        return Response({"status": "OK"}, status=200)
