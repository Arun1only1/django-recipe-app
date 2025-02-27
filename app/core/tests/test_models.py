""" Test case for models"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test Models"""

    def test_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = "arun@gmail.com"
        password = "Arun@123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

