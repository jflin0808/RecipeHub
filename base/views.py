from django.shortcuts import render

# Create your views here.

recipes = [
    {'id': 1, 'name': 'Recipe 1'},
    {'id': 2, 'name': 'Recipe 2'},
    {'id': 3, 'name': 'Recipe 3'},
]

def home(request):
    context = {'recipes': recipes}
    return render(request, 'base/home.html', context)

def recipe(request, pk):
    recipe = None
    for i in recipes:
        if i['id'] == int(pk):
            recipe = i
    context = {'recipe': recipe}
    return render(request, 'base/recipe.html', context)
