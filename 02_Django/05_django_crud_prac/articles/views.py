from django.shortcuts import render
from .models import Article

def index(request):
    articles=Article.objects.order_by('-pk') #번호순으로
    context={'articles':articles}
    return render(request,'articles/index.html',context)


def new(request):
    return render(request,'articles/new.html')

def create(request):
    title=request.GET.get('title')
    content=request.GET.get('content')
    article=Article(title=title,content=content)
    # article.full_clean()
    article.save()

    return render(request,'articles/index.html')

def detail(request,pk):
    article=Article.objects.get(pk=pk)
    context={'article':article}
    return render(request,'articles/detail.html',context)
