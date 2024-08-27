from django.test import TestCase
from rest_framework.exceptions import ValidationError
from .models import Company
from .serializers import CompanyReadSerializer, CompanyReadFullSerializer, CompanyWriteSerializer

class CompanySerializerTest(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name="Test Company",
            description="A test company",
            symbol="TTC",
            alpha_vantage={"some_key": "some_value"}
        )

    def test_company_read_serializer(self):
        serializer = CompanyReadSerializer(instance=self.company)
        data = serializer.data
        self.assertEqual(data['id'], str(self.company.id))
        self.assertEqual(data['name'], self.company.name)
        self.assertEqual(data['description'], self.company.description)
        self.assertEqual(data['symbol'], self.company.symbol)

    def test_company_read_full_serializer(self):
        serializer = CompanyReadFullSerializer(instance=self.company)
        data = serializer.data
        self.assertEqual(data['id'], str(self.company.id))
        self.assertEqual(data['name'], self.company.name)
        self.assertEqual(data['description'], self.company.description)
        self.assertEqual(data['symbol'], self.company.symbol)
        self.assertEqual(data['alpha_vantage'], {"some_key": "some_value"})
        self.assertIn('time_serie', data)

    def test_company_write_serializer_valid(self):
        data = {
            'name': 'New Company',
            'description': 'A new company description',
            'symbol': 'NCC'
        }
        serializer = CompanyWriteSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        company_data = serializer.validated_data
        self.assertEqual(company_data['name'], 'New Company')
        self.assertEqual(company_data['description'], 'A new company description')
        self.assertEqual(company_data['symbol'], 'NCC')

    def test_company_write_serializer_invalid(self):
        data = {
            'name': 'Invalid Company',
            'description': 'Invalid description',
            'symbol': 'INVALID'
        }
        serializer = CompanyWriteSerializer(data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
