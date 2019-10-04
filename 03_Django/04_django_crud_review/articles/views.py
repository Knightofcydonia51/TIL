from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Article

def index(request):
    # articles=Article.objects.all()[::-1]
    articles=Article.objects.order_by('-pk')
    # print(articles)
    # print(type(articles))
    context={'articles':articles}
    return render(request, 'articles/index.html',context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    try:
        title=request.POST.get('title')
        content=request.POST.get('content')
        article= Article(title=title, content=content)
        article.full_clean()

    except ValidationError:
        raise ValidationError('Your Error Message')
    else:
        article.save()
        return redirect('articles:detail', article.pk)


    '''
    #1. 첫번째 방법
    title=request.POST.get('title')
    print(title)
    content=request.POST.get('content')

    # article=Article()
    # article.title = title
    # article.content=content
    # article.save()

    # return render(request, 'articles/create.html')

    #2.두번째 방법
    article=Article(title=title, content=content)
    article.save()

    #3. 세번째 방법
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/index.html')
    return redirect(f'/articles/{article.pk}')
    '''

def detail(request,pk): #pk가 필요한 이유 : 특정한 글을 찾아내야하기 때문
    article=Article.objects.get(pk=pk)
    context={'article':article}
    return render(request, 'articles/detail.html', context)

def delete(request,pk):
    article=Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request,pk):
    article=Article.objects.get(pk=pk)
    context={'article':article}
    return render(request, 'articles/edit.html',context)

def update(request,pk):

    article=Article.objects.get(pk=pk)
    article.title=request.POST.get('title')
    article.content=request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)
