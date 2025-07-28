from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class UserTests(TestCase):
    """ Test the user custom model """
    def test_create_user(self):
        """ Test that a new user can be created """
        # Arrange: Get user model and create details.
        User = get_user_model()
        user_email = 'wasremoved@gmail.com'
        user_password = 'testPassWord123'

        # Act: Create a new user uobject using the  model's manager
        user = User.objects.create_user(
                username='was',
                email=user_email,
                password=user_password
                )

        # Assert: check that user object was created with correct details

        self.assertEqual(user.email, user_email)
        self.assertTrue(user.check_password(user_password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


# API test cases

class UserAPITestCase(APITestCase):
    """ we test all user API endpoints to confirm functionality"""

    def test_create_user_via_api(self):
        """ Are we able to create user objects via the api? """
        # define the URL for creating the user and data for the user
        url = reverse('user-list') 
        data =  {
                'username': 'user1',
                'email': 'user1@email.com',
                'password': 'user1@password'
                }
        # make a POST request using the client
        response = self.client.post(url, data, format='json')

        # confirm if the request was succesful: status code 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # confirm that the user was created in the database
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.get().username, 'user1')
