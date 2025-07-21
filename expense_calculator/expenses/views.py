from rest_framework.viewsets import ModelViewSet
from .serializers import ExpenseSerializer
from .models import Expense

# Create your views here.
class ExpenseViewSet(ModelViewSet):
    """
    Viewset for managing expenses
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


