from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.db.models import Q


# Create your views here.


def article_list(request):
    articles = Article.objects.all()
    query = request.GET.get('q')
    articles = Article.objects.search(query=query)
    # try:
    #     int(query)
    # except:
    #     lookups = Q(title__icontains=query)
    # else:
    #     lookups = Q(title__icontains=query) | Q(id=query)
    # if query:
    #     # articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    #     articles = Article.objects.filter(lookups)
    contex = {
        'object_list': articles,
    }
    return render(request, 'article/index.html', contex)


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        'object': article,
    }
    return render(request, 'article/detail.html', context)


def article_create(request):
    context = {
        'created': False
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        obj = Article.objects.create(title=title, content=content)
        context['created'] = True
        context['object'] = obj

    return render(request, 'article/create.html', context)


def article_create_form(request):
    form = ArticleForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        obj = form.save()
        reverse_url = reverse('article:detail', args=[obj.slug])
        return redirect(reverse_url)
    context = {
        'form': form
    }
    return render(request, 'article/create_form.html', context)


def article_change(request, slug):
    obj = Article.objects.get(slug=slug)
    print(obj)
    form = ArticleForm(instance=obj, files=request.FILES)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=obj, files=request.FILES)
        if form.is_valid():
            obj = form.save()
            reverse_url = reverse('article:detail', args=[obj.slug])
            return redirect(reverse_url)
    context = {
        'form': form,
        'object': obj,
    }
    return render(request, 'article/edit.html', context)


def delete_article(request, slug):
    obj = get_object_or_404(Article, slug=slug)
    # obj = Article.objects.get(slug=slug)
    if request.method == 'POST':
        obj.delete()
        # reverse_url = reverse('article:list', args=[obj.id])
        return redirect('article:list')
    context = {
        'object': obj,
    }
    return render(request, 'article/delete.html', context)
