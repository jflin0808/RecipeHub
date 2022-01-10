from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),

    path('', views.home, name='home'),
    path('recipe/<str:pk>/', views.recipe, name='recipe'),

    path('create-recipe/', views.createRecipe, name='create-recipe'),
    path('update-recipe/<str:pk>/', views.updateRecipe, name='update-recipe'),
    path('delete-recipe/<str:pk>/', views.deleteRecipe, name='delete-recipe'),
    
]