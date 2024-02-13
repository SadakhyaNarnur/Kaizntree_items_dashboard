from django.test import TestCase, Client
from django.urls import reverse
from .models import Itemlist, Category
from .serializers import ItemSerializer, CategorySerializer
import json

class ItemApiTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create sample categories
        Category.objects.create(category_name="Category 1")
        Category.objects.create(category_name="Category 2")

        # Create sample items
        self.item1 = Itemlist.objects.create(SKU="SKU1", Name="Item 1", Tags="Tag1", category=2, In_stock=10, Available_stock=5, user=2)
        self.item2 = Itemlist.objects.create(SKU="SKU2", Name="Item 2", Tags="Tag2", category=2, In_stock=20, Available_stock=15,user=2)

    def test_get_all_items(self):
        response = self.client.get(reverse('item-list'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)

    def test_put_item(self):
        response = self.client.get(reverse('item-id', kwargs={'id': self.item1.pk}))
        self.assertEqual(response.status_code, 200)
        item_data = response.json()
        self.assertEqual(item_data['SKU'], "SKU1")

class CategoryApiTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create sample categories
        self.category1 = Category.objects.create(category_name="Category 1")
        self.category2 = Category.objects.create(category_name="Category 2")

    def test_get_all_categories(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)

    def test_get_single_category(self):
        response = self.client.get(reverse('category-id', kwargs={'id': self.category1.pk}))
        self.assertEqual(response.status_code, 200)
        category_data = response.json()
        self.assertEqual(category_data['name'], "Category 1")

class CountsApiTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create sample categories
        Category.objects.create(category_name="Category 1")
        Category.objects.create(category_name="Category 2")

        # Create sample items
        self.item1 = Itemlist.objects.create(SKU="SKU1", Name="Item 1", Tags="Tag1", category=2, In_stock=10, Available_stock=5, user=2)
        self.item2 = Itemlist.objects.create(SKU="SKU2", Name="Item 2", Tags="Tag2", category=2, In_stock=20, Available_stock=15,user=2)

    def test_counts_api(self):
        response = self.client.get(reverse('counts-api'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['items_count'], 2)
        self.assertEqual(data['categories_count'], 2)
