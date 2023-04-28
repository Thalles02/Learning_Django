from unittest import skip
from django.urls import resolve, reverse
from recipes import views
from recipes.models import *
from .test_recipe_base import RecipeTestBase


# @skip('Pulando os testes a fim de aprendiizado sobre testes unitarios')
class RecipeViewsTest(RecipeTestBase):
    """def tearDown(self) -> None:
        return super().tearDown()"""

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        # Recipe.objects.get(pk=1).delete()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here 🥲</h1>',
            response.content.decode('utf-8')
        )

        # Tenho que digitar algo mais nesse teste em específico
        # self.fail('Termine de codar este test')

    # Criando fixtures para um teste único

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        response_context = response.context['recipes']
        self.assertEqual(response_context.first().title, 'Recipe Title')

        # Caso haja confusão neste teste é apenas para aprendizado mesmo

        response_content = response.content.decode('utf-8')
        self.assertIn('Recipe Title', response_content)
        self.assertIn('10 Minutos', response_content)
        self.assertIn('5 Porções', response_content)
        self.assertEqual(len(response_context), 1)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
