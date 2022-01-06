from django.contrib import admin

# Register your models here.

from .models import Recipe, Tag, Diet, Meal

admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Diet)
admin.site.register(Meal)