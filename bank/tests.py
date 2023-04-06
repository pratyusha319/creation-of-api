from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from bank.models import *
from bank.serializers import*

# initialize the APIClient app
client = APIClient()

class BankTests(APITestCase):
    def setUp(self):
        self.bank1 = Bank.objects.create(name="Bank of America")
        self.bank2 = Bank.objects.create(name="Chase Bank")
        self.branch1 = Branch.objects.create(
            ifsc="BOFA000001",
            branch="Main Branch",
            address="123 Main Street",
            city="New York",
            district="Manhattan",
            state="NY",
            bank=self.bank1
        )
        self.branch2 = Branch.objects.create(
            ifsc="CHAS000002",
            branch="Downtown Branch",
            address="456 Downtown Street",
            city="Los Angeles",
            district="Downtown",
            state="CA",
            bank=self.bank2
        )

    def test_get_all_banks(self):
        # get API response
        response = client.get(reverse('bank_list'))
        # get data from db
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_branch_details(self):
        # get API response
        response = client.get(reverse('branch_details', kwargs={'ifsc': self.branch1.ifsc}))
        # get data from db
        branch = Branch.objects.get(ifsc=self.branch1.ifsc)
        serializer = BranchSerializer(branch)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_branch_details(self):
        # get API response
        response = client.get(reverse('branch_details', kwargs={'ifsc': 'INVALID_IFSC_CODE'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
