from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.    
class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=20, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.amount} from {self.source}"


class Expense(models.Model):
    GROCERIES = "GROCERIES"
    RENT = "RENT"
    OTHER = 'OTHER'
    CATEGORIES = [
        (GROCERIES, "Grocery"),
        (RENT, "Rent"),
        (OTHER, "Other"),
    ]
    category = models.CharField(max_length=10, choices=CATEGORIES, default=OTHER)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)