from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Diet(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    diet = models.ForeignKey(Diet, on_delete=models.SET_NULL, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField()
    preparation = models.TextField()
    prep_time = models.DurationField()
    instructions = models.TextField()
    cook_time = models.DurationField()
    servings = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
