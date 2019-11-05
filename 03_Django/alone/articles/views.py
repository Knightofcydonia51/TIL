from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from IPython import embed

def index(request):
    articles=Article.objects.all()
    context={
        'articles':articles,
    }
    return render(request, 'articles/index.html',context)


def create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        article=Article.objects.create(title=title,content=content)
        article.save()
        return redirect('articles:index')
    else:
        return render(request, 'articles/create.html')

def detail(request,article_pk):
    article=Article.objects.get(pk=article_pk)
    context={'article':article,}
    return render(request,'articles/detail.html',context)

def update(request, article_pk):
    article=Article.objects.get(pk=article_pk)
    context={
        'article':article,
    }
    return render(request, 'articles/update.html',context)

def edit(request,article_pk):
    article=Article.objects.get(pk=article_pk)
    if request.method=='POST':
        article.title=request.POST.get('title')
        article.content=request.POST.get('content')
        article.save()
        return redirect('articles:detail',article_pk)

def delete(request,article_pk):
    if request.method=='POST':
        article=Article.objects.get(pk=article_pk)
        article.delete()
        return redirect('articles:index')

        

    