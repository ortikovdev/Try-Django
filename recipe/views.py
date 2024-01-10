from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import RecipeForm
from .models import Recipe, Tag, Ingredient


def recipe_list(request):
    recipes = Recipe.objects.order_by('-id')
    tag = request.GET.get('tag')
    if tag:
        recipes = Recipe.objects.order_by('id').filter(tags__title=tag)
    context = {
        'object_list': recipes
    }
    return render(request, 'recipe/index.html', context)


def my_recipe_list(request):
    recipes = Recipe.objects.filter(author_id=request.user.id).order_by('-id')
    tag = request.GET.get('tag')
    if tag:
        recipes = Recipe.objects.order_by('id').filter(tags__title=tag)
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


def recipe_create(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False, )
            obj.author_id = request.user.id
            obj.save()
            detail_url = reverse('recipe:detail', args=[obj.slug])
            return redirect(detail_url)
    context = {
        "form": form,
    }
    return render(request, 'recipe/create.html', context)
