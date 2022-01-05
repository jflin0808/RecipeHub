from django.shortcuts import render
from .models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'base/home.html', context)

def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    context = {'recipe': recipe}
    return render(request, 'base/recipe.html', context)
