from django.test import TestCase
from .models import Company

class CompanyModelTest(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name="Test Company",
            description="A test company",
            symbol="TTC",
            alpha_vantage={"some_key": "some_value"}
        )

    def test_company_creation(self):
        company = Company.objects.get(symbol="TTC")
        self.assertEqual(company.name, "Test Company")
        self.assertEqual(company.description, "A test company")
        self.assertEqual(company.symbol, "TTC")
        self.assertEqual(company.alpha_vantage, {"some_key": "some_value"})
