from django.contrib import admin

# Register your models here.
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'timestamp', 'category')
    search_fields = ('timestamp',)
    list_filter = ('timestamp',)

