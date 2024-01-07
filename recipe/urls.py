from django.urls import path
from .views import (
    recipe_list,
    recipe_detail,
    my_recipe_list,
    recipe_create
)

app_name = 'recipe'

urlpatterns = [
    path('list/', recipe_list, name='list'),
    path('detail/<slug:slug>', recipe_detail, name='detail'),
    path('list/my/', my_recipe_list, name='my-list'),
    path('create/', recipe_create, name='create')
]