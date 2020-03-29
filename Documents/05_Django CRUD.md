### CRUD 다뤄보자

basic settings!!!

```
python -m venv venv
source venv/Scripts/activate
django-admin startproject crud .
python manage.py startapp articles
출생신고 : crud -> settings.py -> INSTALLED_APPS
```

```
# 프로젝트안에 urls.py 작성
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls'))
    path('admin/', admin.site.urls),
]
```

```
# 앱안에 urls.py 작성;
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
]
```

```
# basic.html 작성
```

```
# 모델
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'
```

```
python manage.py makemigrations
python manage.py migrate
```

```
# views.py
from django.shortcuts import render, redirect
from .models import Article

def index(request):
    #articles = Article.object.all()[::-1]
    articles = Article.objects.order_by('-id')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('/articles')
```

```
# index
{% extends 'base.html' %}

{% block body %}
    <h1 class="text-center">Articles</h1>
    <hr>
    {% for article in articles %}
        <p>글 번호: {{ article.id }}</p>
        <p>글 제목: {{ article.title }}</p>
        <p>글 내용: {{ article.content }}</p>
        <hr>
    {% endfor %}
    <a href="/articles/new/">[글쓰기]</a>
{% endblock %}
```

```
# new.html
{% extends 'base.html' %}

{% block body %}
    <h1 class="text-center">NEW PAGE</h1>
    <form action="/articles/create/" method="POST">
        {% csrf_token %}
        <label for="title">Title</label><br>
        <input type="text" id="title" name="title"><br>
        <label for="content">Content</label><br>
        <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
        <input type="submit" value="글쓰기">
    </form>
    <a href="/articles/" target="_blank">[메인 페이지로 돌아가기]</a>
{% endblock %}
여기서 _blank는 새창에서 띄우기
```

```
# create.html
{% extends 'base.html' %}

{% block body %}
    <h1 class="text-center">글이 성공적으로 작성되었습니다.</h1>
{% endblock %}
```



models 만들고 메이크 마이그레이션, 마이그레이트, urls만들고, views 만듬

