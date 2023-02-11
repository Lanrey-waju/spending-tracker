from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Income

User = get_user_model()

# Create your tests here.
class TrackerModelTests(TestCase):
    """
    Tests the Income Model
    """
    def setUp(self):
        self.user = User.objects.create_user(email="user@user.com", first_name="user", password="foo")
        self.income = Income.objects.create(amount=3.33, source="Salary", user=self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.income), "3.33 from Salary")
    
    def test_user_can_create_income_instance(self):
        self.assertEqual(self.income.user, self.user)

    def test_income_model(self):
        # income = Income.objects.create(amount=3.33, source="Salary")
        self.assertEqual(self.income.amount, 3.33)
        self.assertEqual(self.income.source, "Salary")
