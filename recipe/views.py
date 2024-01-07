from django.shortcuts import render, get_object_or_404

from .models import Recipe, Tag, Ingredient


def recipe_list(request):
    recipes = Recipe.objects.order_by('-id')
    context = {
        'object_list': recipes
    }
    return render(request, 'recipe/index.html', context)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    ingredients = Ingredient.objects.filter(recipe=recipe)
    is_author = request.user == recipe.author
    context = {
        "object": recipe,
        "ingredients": ingredients,
        "is_author": is_author
    }
    return render(request, 'recipe/detail.html', context)


def recipe_edit(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)