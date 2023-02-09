from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class UserManagerTests(TestCase):
    """
    Tests the Custom User Manager for creating and saving users
    """
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="user@user.com", first_name="user1", password="foo")
        self.assertEqual(user.email, "user@user.com")
        self.assertEqual(user.first_name, "user1")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

        try:
            # username does not exist
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", first_name="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="user@user.com", first_name="", password="foo")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", first_name="user1", password="foo")

    def test_create_superuser(self):
        """
        Tests creation of user with superuser privileges
        """
        User = get_user_model()
        superuser = User.objects.create_superuser(email="admin@user.com", first_name="admin", password="foo")
        self.assertEqual(superuser.email, "admin@user.com")
        self.assertEqual(superuser.first_name, "admin")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_superuser)

        try:
            # Ensure username doesn't exist
            self.assertIsNone(superuser.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="admin@user.com", first_name="admin", password="foo", is_superuser=False)

        