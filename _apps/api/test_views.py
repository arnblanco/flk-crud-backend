from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Company

class CompanyViewSetTest(APITestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name="Test Company",
            description="A test company",
            symbol="TTC",
            alpha_vantage={"some_key": "some_value"}
        )
        self.url = reverse('company-list')

    def test_list_companies(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['symbol'], self.company.symbol)

    def test_create_company(self):
        data = {
            'name': 'New Company',
            'description': 'A new company description',
            'symbol': 'NCC'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['symbol'], 'NCC')

    def test_retrieve_company(self):
        url = reverse('company-detail', args=[self.company.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['symbol'], self.company.symbol)

    def test_update_company(self):
        url = reverse('company-detail', args=[self.company.id])
        data = {
            'name': 'Updated Company',
            'description': 'Updated description',
            'symbol': 'UTC'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Company')

    def test_delete_company(self):
        url = reverse('company-detail', args=[self.company.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Company.objects.count(), 0)
