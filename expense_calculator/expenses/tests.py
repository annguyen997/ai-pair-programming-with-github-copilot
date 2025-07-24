from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Expense
# Create your tests here.
class ExpenseTestCase(APITestCase):
    def setUp(self):
        # Create 3 expenses for testing
        Expense.objects.bulk_create([
            Expense(name="Test Expense 1", amount=100.00, category='Food'),
            Expense(name="Test Expense 2", amount=200.00, category='Transport'),
            Expense(name="Test Expense 3", amount=300.00, category='Utilities'),
        ])
    
    def test_expense_list(self):
        """
        Test the expense list endpoint
        """
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_expense_detail(self):
        """
        Test the expense detail endpoint
        """
        response = self.client.get('/api/expenses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'Food')
        self.assertEqual(response.json()['amount'], 10.00)
        self.assertEqual(response.json()['category'], 'Food')

    def test_expense_create(self):
        data = {
            'name': 'Food',
            'amount': 150.00,
            'category': 'Food'
        }
        response = self.client.post('/api/expenses/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], 'Food Item')
        self.assertEqual(response.json()['amount'], 150.00)
        self.assertEqual(response.json()['category'], 'Food')
    
    def test_expense_update(self):
        """
        Test updating an existing expense
        """
        expense = Expense.objects.first()
        data = {
            'name': 'Updated Expense',
            'amount': 250.00,
            'category': 'Transport'
        }
        response = self.client.put(f'/api/expenses/{expense.id}/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], data['name'])
        self.assertEqual(response.json()['amount'], str(data['amount']))
        self.assertEqual(response.json()['category'], data['category'])
    
    def test_expense_delete(self):
        """
        Test deleting an expense
        """
        response = self.client.delete('/api/expenses/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Expense.objects.all()), 2)
        self.assertRaises(Expense.DoesNotExist, Expense.objects.get, pk=1)
        response = self.client.delete('/api/expenses/2/')
        self.assertEqual(response.status_code, 204)

    def tearDown(self):
        Expense.objects.all().delete()