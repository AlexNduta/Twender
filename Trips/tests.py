from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Trip
class TestTripModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Setup an object """
        # we first create a user
        User = get_user_model()
        test_user = User.objects.create_user(
                username='test_user',
                password='testpassword'
                )
        # create a trip object using the user object
        Trip.objects.create(
                passenger=test_user,
                pickup_location="Juja",
                drop_off_location="CBD",
                fare=70,
                seat_number=1,
                payment_status='pending'
                )
    def test_trip_creation(self):
        """test that the trip was created with the correct data """
        # get the trip frf the test database
        trip =Trip.objects.get(id=1)

        self.assertEqual(trip.pickup_location, 'Juja')
        self.assertEqual(trip.passenger.username, 'test_user')
        self.assertEqual(trip.payment_status, 'pending')
    
