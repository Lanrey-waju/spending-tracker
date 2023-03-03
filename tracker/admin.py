from django.contrib import admin

from .models import Expense, Income

# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    pass

class IncomeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income, IncomeAdmin)