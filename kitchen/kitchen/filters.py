from django_filters import FilterSet, ModelChoiceFilter
from .models import Recipe, Category


class RecipeFilter(FilterSet):

    Category = ModelChoiceFilter(
        field_name='RecipeCategory',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='ALL',
    )

    class Meta:
        model = Recipe
        fields = {
            'title': ['icontains'],
        }

