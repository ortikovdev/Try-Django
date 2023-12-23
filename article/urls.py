from django.urls import path
from .views import (
    article_list,
    article_detail,
    article_create,
    article_create_form,
    article_change,
    delete_article
)

app_name = 'article'

urlpatterns = [
    path('', article_list, name='list'),
    path('article/create/', article_create, name='create'),
    path('article/create_form/', article_create_form, name='create_form'),
    path('article/change/form/<slug:slug>/', article_change, name='change_form'),
    path('article/delete/form/<slug:slug>/', delete_article, name='delete'),
    path('article/<slug:slug>/', article_detail, name='detail'),
]
