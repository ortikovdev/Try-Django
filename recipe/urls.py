from django.urls import path
from .views import recipe_list

app_name = 'recipe'

urlpatterns = [
    path('list/', recipe_list, name='list')
]