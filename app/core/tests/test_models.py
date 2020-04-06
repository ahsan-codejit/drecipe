from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@test.com'
        password = '12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the new user email is normalized"""
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='132454'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating new super user"""
        user = get_user_model().objects.create_superuser(
            email="super@test.com",
            password="12345"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
