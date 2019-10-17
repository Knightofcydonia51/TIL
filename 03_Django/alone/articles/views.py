from django.shortcuts import render
from models import Article

def index(request):
    return render(request, 'articles/index.html')


def create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        Article.objects.create(title=title,content=content)