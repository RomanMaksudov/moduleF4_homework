from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView
)
from .models import Recipe, Category
from .filters import RecipeFilter
from .forms import RecipeForm

from django.db.models import Exists, OuterRef
from django.shortcuts import render


class RecipeList(ListView):
    model = Recipe
    ordering = 'title'
    template_name = 'kitchen.html'
    context_object_name = 'kitchen'
    paginate_by = 10


class RecipeDetail(DetailView):
    model = Recipe
    template_name = 'recipe.html'
    context_object_name = 'recipe'

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.filterset = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = RecipeFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class RecipeSearch(ListView):
    model = Recipe
    template_name = 'recipe_search.html'
    context_object_name = 'kitchen'
    filterset_class = RecipeFilter
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = RecipeFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['category'] = Category.objects.all()
        return context


class RecipeCreate(CreateView):
    raise_exception = True
    form_class = RecipeForm
    model = Recipe
    template_name = 'recipe_edit.html'
    # recipe: object = form.save(commit=False)
    # recipe.categoryType = 'M'
    # return super().form_valid(form)


class RecipeUpdate(UpdateView):
    form_class = RecipeForm
    model = Recipe
    template_name = 'recipe_edit.html'

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.categoryType = 'M'
        return super().form_valid(form)

