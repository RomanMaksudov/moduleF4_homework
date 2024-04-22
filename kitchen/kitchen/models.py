from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Recipe(models.Model):

    MEAT = 'M'
    FISH = 'F'
    CATEGORY_CHOICES = (
        (MEAT, 'Мясо'),
        (FISH, 'Рыба'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=MEAT)
    recipeCategory = models.ManyToManyField(Category, through='RecipeCategory')
    title = models.CharField(max_length=128, default='Steak')
    text = models.TextField()

    def preview(self):
        return self.text[0:123] + '...'

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])


class RecipeCategory(models.Model):
    recipeThrough = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
