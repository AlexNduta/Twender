from django.test import TestCase
from django.contrib.auth import get_user_model


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


