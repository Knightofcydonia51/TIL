from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Article, Comment
from IPython import embed

def index(request):
    # articles=Article.objects.all()[::-1]
    articles=Article.objects.order_by('-pk')
    # print(articles)
    # print(type(articles))
    context={'articles':articles}
    return render(request, 'articles/index.html',context)

# def new(request):
#     embed()
#     return render(request, 'articles/new.html')

def create(request):
    # POST 요청일 때 
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        image=request.FILES.get('image')
        
        article= Article(title=title, content=content, image=image)
        article.full_clean()
        article.save()
        # embed()
        return redirect('articles:detail', article.pk)
    # GET 요청일 때
    else:
        return render(request,'articles/create.html')
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

def detail(request, article_pk): #pk가 필요한 이유 : 특정한 글을 찾아내야하기 때문
    article=Article.objects.get(pk=article_pk)
    comments=article.comments.all()
    context={'article':article, 'comments':comments}
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    if request.method=='POST':
        article=Article.objects.get(pk=article_pk)
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:index',article_pk)

# def edit(request,pk):
#     article=Article.objects.get(pk=pk)
#     context={'article':article}
#     return render(request, 'articles/edit.html',context)

def update(request,article_pk):
    # embed()
    article=Article.objects.get(pk=article_pk)
    if request.method=='POST':
        article.title=request.POST.get('title')
        article.content=request.POST.get('content')
        article.image=request.FILES.get('image')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context={'article':article}
        return render(request,'articles/edit.html',context)

def comments_create(request, article_pk):
    article=Article.objects.get(pk=article_pk)
    if request.method=='POST':
        # content=request.POST.get('content')

        comment=Comment(article=article, content=request.POST.get('content'))
        comment.save()

        return redirect('articles:detail',article_pk)

    else:
        return redirect('articles:detail',article.pk)

def comments_delete(request, article_pk,comment_pk):
    if request.method=='POST':
        comment=Comment.objects.get(pk=comment_pk)
        comment.delete()

    return redirect('articles:detail', article_pk)

def comments_update(request, article_pk, comment_pk):
    comment=Comment.objects.get(pk=comment_pk)
    if request.method=='POST':
        comment.content=request.POST.get('content')
        comment.save()
        return redirect('articles:detail',article_pk)
    else:
        context={'comment':comment}
        return render(request,'articles/comments_update.html',context)