from django.test import TestCase
from django.urls import reverse

# Create your tests here.

# Introdução aos teste Unitários


class RecipeURLsTest(TestCase):

    def test_pytest_ok(self):
        print('Hello World!')
        assert 1 == 1, 'Um é igual a um'

    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        # pode usar o args=(1,) ou o kwargs={'category_id': 1}
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1')

    def test_recipe_detail_url_is_correct(self):
        # pode usar o args=(1,) ou o kwargs={'category_id': 1}
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1')
