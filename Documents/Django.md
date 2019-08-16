# Django

- 파이썬 기반의 웹프레임워크

>프레임워크를 사용한다는 것은 프랜차이즈 창업과도 비슷함.
>
>기본적인 양식이 사용자에게 주어짐.





## MTV 양식

>Model : 데이터를 관리
>
>Template : 사용자가 보는 화면
>
>View : 중간 관리자



## 명령어

- gitignore.io 에서 Django를 검색하여 gitignore환경을 먼저 세팅한 뒤 작업한다.

> python -m venv venv
>
> source venv/Scripts/activate (가상환경 생성)
>
> deactivate (해제)
>
> pip list 명령어로 현재 작동중인지 확인 가능. (작동중이라면 2개만나옴. pip, setuptools)



## 설치

> activate 상태에서 pip install Django 입력
>
> pip list로 설치 확인 가능.
>
> python -m pip install django  (Fatal error 발생시)



## 본격적인 사용

> django-admin startproject 프로젝트명 .  >프로젝트 시작
>
> python manage.py runserver
>
> **ctrl + c : 종료**
>
> python manage.py startapp pages : 앱 만들기

venv의 상위 경로에서 select interpreter로 들어가서 venv 선택하면 자동으로 환경 잡아줌.



### 각 파일의 역할

- settings.py : 세팅 변경
- urls.py : 경로 확인 (집배원)
- views.py : request를 받고 프로젝트의 데이터를 중계.

장고는 1개의 프로젝트와 다양한 app으로 구성됨.



## Settings.py

>INSTALLED_APPS : 설치된 앱들을 확인 및 수정, app을 만들고 나면 여기에 앱의 이름을 추가해주어야한다. ex) pages
>
>LANGUAGE_CODE : 언어 확인 및 수정 (ko-kr : 한국)
>
>TIME_ZONE : 기준 시간 변경 (Asia/Seoul)



### 01_django_intro의 구조

>django_intro : 프로젝트로, 하위 앱들을 관리해주는 setting을 가지고 있음.
>
>pages, utilities : 하위 앱들.



### 상속

>상속받고 싶은 파일을 프로젝트 폴더(ex : django_intro)의 templates 안에 위치시킨다. 
>
>TEMPLATES의 'DIRS' 밸류값을
>
>[os.path.join(BASE_DIR, '해당 프로젝트 폴더명', 'templates')],



# Model 구축

>프로젝트환경 구축, 앱 만든 이후부터
>
>models. py 만들기
>
>```python
>from django.db import models
>
>class Article(models.Model):
>    title=models.CharField(max_length=10)
>    content = models.TextField()
>    created_at=models.DateTimeField(auto_now_add=True)
>```
>
>python manage.py makemigrations
>
>python manage.py migrate
>
>python manage.py shell
>
>(쉘 들어온 다음)
>
>from (앱이름).models import (클래스이름)
>
>

## 예시

```python
>>> from articles.models import Article    # 이친구는 다시 켤때마다 해줘야함.
>>> Article.objects.all()
<QuerySet []>
>>> article=Article()
>>> article.title = 'first'
>>> article.content = 'django!'
>>> article
<Article: Article object (None)>
>>> article.save()
>>> article
<Article: Article object (1)>
>>> article.title
'first'
>>> article.content
'django!'
>>> article.created_at
datetime.datetime(2019, 8, 7, 7, 10, 13, 176802, tzinfo=<UTC>)
>>> article=Article(title='second', content='django!')
>>> article
<Article: Article object (None)>
>>> article.save()
>>> article
<Article: Article object (2)>
>>> Article.objects.get(pk=1)
<Article: Article object (1)>
>>> articles=Article.objects.all()
>>> articles
<QuerySet [<Article: Article object (1)>, <Article: Article object
(2)>]>
>>> Article.objects.create(title='third',content='django!')
<Article: Article object (3)>

>>> article=Article()
>>> article
<Article: Article object (None)>
>>> article.title='fourth'
>>> article.content='django!'
>>> article.title
'fourth'
>>> article.id
>>> article.save()
>>> article.id
4
>>> article=Article()
>>> article.full_clean()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\TIL\03_Django\02_django_query\venv\lib\site-packages\django\db\models\base.py", line 1203, in full_clean
    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'title': ['이 필드는 빈 칸
으로 둘 수 없습니다.'], 'content': ['이 필드는 빈 칸으로 둘 수 없습
니다.']}
>>> article.title='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
>>> article
<Article: Article object (None)>

>>> article.full_clean()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\TIL\03_Django\02_django_query\venv\lib\site-packages\django\db\models\base.py", line 1203, in full_clean    raise ValidationError(errors)
django.core.exceptions.ValidationError: {'title': ['이 값이 최대 10 개의 글자인지 확인하세요(입력값 39 자).'], 'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
                                                   
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>, <Article: Article object (4)>]>
                                                   
>>> exit()
                                                   
>>> from articles.models import Article
>>> articles = Article.objects.all()
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 2번글 - second: django!>, <Article: 3번글 - third: django!>, <Article: 4번글 - fourth: django!>]>
>>> type(articles)
<class 'django.db.models.query.QuerySet'>
>>> Article.objects.create(title='first', content='hahaha')
<Article: 5번글 - first: hahaha>

>>> articles=Article.objects.filter(title='first')
>>> articles
<QuerySet [<Article: 1번글 - first: django!>, <Article: 5번글 - first: hahaha>]>
>>> Article.objects.create(title='first', content='vacation')
<Article: 6번글 - first: vacation>
>>> article=Article.objects.filter(title='first').first()
>>> article
<Article: 1번글 - first: django!>
>>> article= Article.objects.filter(title='first').last()
>>> article
<Article: 6번글 - first: vacation>
>>> article=Article.objects.get(pk=1)
>>> article
<Article: 1번글 - first: django!>
>>> article = Article.objects.get(title='first')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\student\TIL\03_Django\02_django_query\venv\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\student\TIL\03_Django\02_django_query\venv\lib\site-packages\django\db\models\query.py", line 412, in gete-packages\django\db\models\query.py", line 412, in get
    (self.model._meta.object_name, num)                            e than one Article -- it returned 3!
articles.models.Article.MultipleObjectsReturned: get() returned more than one Article -- it returned 3!
>>> article=Article.objects.get(pk=10)
Traceback (most recent call last):                                 e-packages\django\db\models\manager.py", line 82, in manager_method
  File "<console>", line 1, in <module>
  File "C:\Users\student\TIL\03_Django\02_django_query\venv\lib\site-packages\django\db\models\query.py", line 408, in gete-packages\django\db\models\manager.py", line 82, in manager_method                                                                   ot exist.
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\student\TIL\03_Django\02_django_query\venv\lib\site-packages\django\db\models\query.py", line 408, in get
    self.model._meta.object_name
articles.models.Article.DoesNotExist: Article matching query does not exist.
>>> article = Article.objects.filter(pk=10)
>>> article
<QuerySet []>
```



- 관리자 계정 생성

> python manage.py createsuperuser



- django-extensions 설치

> pip install django-extensions
>
> INSTALLED_APPS에 'django_extensions', 맨 아래줄에 추가.
>
> python manage.py shell_plus 로 실행
>
> 이걸 쓰면 import 안해줘도 됨.



### 값 추가하는 3가지 방법

```python
>>> article=Article()
>>> article.title='hoho'
>>> article.content='hihi'
>>> article.save()

>>> article=Article(title='letit', content='be')
>>> article.save()

>>> Article.objects.create(title='kokoko', content='zzz')

```



