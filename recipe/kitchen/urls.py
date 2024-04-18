from django.urls import path
from . import views

urlpatterns = [
    path('api/kitchen/', views.RecipeListCreate.as_view() ),
]