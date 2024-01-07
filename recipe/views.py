from django.shortcuts import render

from .models import Recipe, Tag, Ingredient


def recipe_list(request):
    recipes = Recipe.objects.order_by('-id')
    context = {
        'object_list': recipes
    }
    return render(request, 'recipe/index.html', context, recipes)