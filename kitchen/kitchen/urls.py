from django.urls import path, include
from .views import (
   RecipeList, RecipeDetail, RecipeSearch, RecipeCreate, RecipeUpdate,
)
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('i18n/', include('django.conf.urls.i18n')),
   path('', RecipeList.as_view(), name='kitchen'),
   path('<int:pk>', cache_page(60*10)(RecipeDetail.as_view()), name='recipe_detail'),
   path('search/', RecipeSearch.as_view(), name='recipe_search'),
   path('create/', RecipeCreate.as_view(), name='recipe_create'),
   path('<int:pk>/edit/', RecipeUpdate.as_view(), name='recipe_edit'),
]
