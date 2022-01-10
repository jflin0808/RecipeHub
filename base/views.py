from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Recipe, Diet
from .forms import RecipeForm

# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password Incorrect')
    context={'page':page}
    return render(request, 'base/account.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occurred while registering')

    context = {'form':form}
    return render(request, 'base/account.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    recipes = user.recipe_set.all()
    diets = Diet.objects.all()
    context = {'user': user, 'recipes':recipes, 'diets':diets,}
    return render(request, 'base/profile.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else ''

    # Filter Search Query by diet name, not case sensitive
    recipes = Recipe.objects.filter(
        Q(diet__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    recipe_count = recipes.count()
    diets = Diet.objects.all()
    context = {'recipes': recipes, 'diets': diets, 'recipe_count': recipe_count}
    return render(request, 'base/home.html', context)


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    context = {'recipe': recipe}
    return render(request, 'base/recipe.html', context)


@login_required(login_url='login')
def createRecipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/recipe_form.html', context)


@login_required(login_url='login')
def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = RecipeForm(instance=recipe)
    
    if request.user != recipe.user:
        return HttpResponse('You are not allowed to update this room')
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/recipe_form.html', context)


@login_required(login_url='login')
def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    context = {'obj':recipe}

    if request.user != recipe.user:
        return HttpResponse('You are not allowed to update this room')

    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    return render(request, 'base/delete.html', context)