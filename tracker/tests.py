from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

from .models import Income, Expense

User = get_user_model()

# Create your tests here.
class TrackerModelTests(TestCase):
    """
    Tests the Income Model
    """
    def setUp(self):
        self.user = User.objects.create_user(email="user@user.com", first_name="user", password="foo")
        self.income = Income.objects.create(amount=3.33, source="Salary", user=self.user, date=timezone.now())
        self.expense = Expense.objects.create(amount=2.00, date=timezone.now())


    def test_string_representation(self):
        self.assertEqual(str(self.income), "3.33 from Salary")
        self.assertEqual(str(self.expense), "2.0 on OTHER")
    
    def test_user_can_create_income_instance(self):
        self.assertEqual(self.income.user, self.user)

    def test_income_model(self):
        # income = Income.objects.create(amount=3.33, source="Salary")
        self.assertEqual(self.income.amount, 3.33)
        self.assertEqual(self.income.source, "Salary")
    
    def test_expense_model(self):
        self.assertEqual(self.expense.amount, 2.00)
        self.assertEqual(self.expense.category, "OTHER")


