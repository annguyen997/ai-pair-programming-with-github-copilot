from django.contrib import admin

# Register your models here.
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'timestamp', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'timestamp')
    ordering = ('-timestamp',)

    