from django.db import models

# Create your models here.
class Expense(models.Model):
    """
    Expense model
    """
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ${self.amount} on {self.date}"

