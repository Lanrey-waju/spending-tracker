from django.db import models

# Create your models here.
class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.amount} from {self.source}"