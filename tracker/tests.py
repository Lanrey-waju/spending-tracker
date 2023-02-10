from django.test import TestCase

from .models import Income

# Create your tests here.
class TrackerModelTests(TestCase):
    """
    Tests the Income Model
    """
    def setUp(self):
        self.income = Income.objects.create(amount=3.33, source="Salary")

    def test_income_model(self):
        # income = Income.objects.create(amount=3.33, source="Salary")
        self.assertEqual(self.income.amount, 3.33)
        self.assertEqual(self.income.source, "Salary")
