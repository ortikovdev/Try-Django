import random

from django.shortcuts import HttpResponse
from article.models import Article


def greeting(request):
    obj_id = random.randint(1, 5)
    print("greeting project is working")
    print(obj_id)
    article = Article.objects.get(id=obj_id)
    title = f'<h1>{article.title} ({obj_id})</h1>'
    content = f"<h2>{article.content}</h2>"
    html_string = title + content
    return HttpResponse(html_string)
