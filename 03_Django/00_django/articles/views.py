from django.shortcuts import render, redirect
from .forms import ArticleForm


def index(request):
    
    return render(request, 'articles/index.html')

def create(request):
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('articles:index')
    else:
        form=ArticleForm()
    context={'form':form,}
    return render(request, 'articles/form.html',context)
    
# def detail(request, article_pk):
    
        

