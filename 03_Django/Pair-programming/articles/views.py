from django.shortcuts import render, redirect
from .models import Article, Comment
from IPython import embed

def index(request):
    articles = Article.objects.all()
    context={
        'articles':articles
    }
    # embed()
    return render(request, 'articles/index.html',context)

def create(request):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article=Article.objects.create(title=title, content=content)
        article.save()
        # embed()
        return redirect('articles:index')
    else:
        return render(request,'articles/create.html')
    
def detail(request, article_pk):
    # embed()
    article = Article.objects.get(pk= article_pk)
    comments = Comment.objects.all()

    context= {'article': article, 'comments':comments}
    
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    if request.method=='POST':
        article=Article.objects.get(pk= article_pk)
        article.delete()
        return redirect('articles:index')


def update(request, article_pk):
    article = Article.objects.get(pk= article_pk)
    context= {'article': article,}
    # embed()
    return render(request, 'articles/update.html', context)

def edit(request, article_pk):
    article =Article.objects.get(pk= article_pk)
    if request.method=='POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        
        return redirect('articles:detail', article_pk)

def comment_create(request, article_pk):
    
    article =Article.objects.get(pk= article_pk)
    if request.method=='POST':
        content = request.POST.get('content')
        # embed()
        comment = Comment()
        comment.content = content 
        comment.article_id = article.pk
        comment.save()
        # embed()
        return redirect('articles:detail', article_pk)

        
def comment_delete(request, article_pk, comment_pk):
    if request.method=='POST':
        # embed()
        comment=Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)



