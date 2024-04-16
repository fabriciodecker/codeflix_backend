from django.urls import reverse
import pytest
from rest_framework import status
from rest_framework.test import APITestCase
from src.core.category.domain.category import Category

# from src.django_project.category_app.repository import DjangoORMCategoryRepository


@pytest.mark.django_db
class TestCategoryAPI(APITestCase):
   def test_list_categories(self):
      url = "/api/categories/"
      response = self.client.get(url)
      expected_data = [
          {
                "id": "xxxclkjçadsf",
                "name": "Movie",
                "description": "Movie description",
                "is_active": True
            },
            {
                "id": "adsfxxxclkjçadsfad",
                "name": "Documentary",
                "description": "Documentary description",
                "is_active": True
            }
      ]
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.data, expected_data)