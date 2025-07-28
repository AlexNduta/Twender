from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Trip
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


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
  
class TripAPITests():
    """ Test that all our trips API endpoints are working as expected """
    @classmethod
    def setupTestdata(cls):
        # create a user(passanger)
        cls.user = get_user_model().objects.create_user(
                username='passanger1', password='testpassword'
                )
    def test_create_trip_via_api(self):
        """ Can Our user create a new trip? """

        # Authenticate our user
        self.client.force_authenticate(user=self.User)

        # Define the URL an data of the new trip
        url = reverse('trip-list')
        data = {
                'passanger': self.user.id,
                'pickup_loctaion': 'Westlands',
                'drop_off_location': kinoo,
                'fare': 50,
                'seat_number': 5
                }
        # make a POST request
        response = self.client.post(url, data, format='json')

        # Assert that the trip was created sucessfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trip.objects.count(), 1)
        self.assertEqual(Trip.objects.get().pickup_location, 'Westlands')
