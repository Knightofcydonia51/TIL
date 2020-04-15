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
>title=models.CharField(max_length=10)
>content = models.TextField()
>created_at=models.DateTimeField(auto_now_add=True)
>
>class Meta:
>ordering=('-pk',) # 순서결정
>```
>
>python manage.py makemigrations
>
>python manage.py migrate
>
>python manage.py sqlmigrate 앱이름 0001
>
>python manage.py shell
>
>(쉘 들어온 다음)
>
>from (앱이름).models import (클래스이름)
>
>```python
>class ArticleForm(forms.ModelForm):
>     class Meta:
>        model = Article
>        fields = ('title','content',)
>
>```
>
>






## 관리자 계정(admin.py)

>python manage.py createsuperuser(관리자 계정 생성)
>
>model을 form을 이용해 표현하고자 할 때는 이곳에도 설정 필요.
>
>
>
>admin.py 에서
>
>```python
>from django.contrib import admin
>from .models import Article
>
>@admin.register(Article)
>class ArticleAdmin(admin.ModelAdmin):
>list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
>
>
># admin.site.register()
>
>```
>
>설정 후 views.py에 
>
>from .forms import ArticleForm
>
>같은식으로 임포트 후 사용.



## urls.py

>프로젝트 폴더 urls.py에 include설정
>
>앱 폴더에 url.py 만들고, 주소 설정
>
>from . import views
>





## 예시

```python
CREATE (create 함수 사용, POST로 받아서 사용할 것.)

if request.method=='POST':
	title=request.POST.get('title')
	content=request.POST.get('content')
    article=Article.objects.create(title=title, content=content)
    article.save()
    return redirect('articles:index')
else:
    return render(request,'articles/create.html')

```



- django-extensions 설치

> pip install django-extensions
>
> INSTALLED_APPS에 'django_extensions', 맨 아래줄에 추가.
>
> python manage.py shell_plus 로 실행
>
> 이걸 쓰면 import 안해줘도 됨.



### 이미지

```
pip install Pillow

```



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



### 쓸만한 익스텐션

```
polacode : 코드 사진파일로 저장할때
icons : 파일 아이콘으로 보여줌
```



### 장고 ORM 연습

```python
user1 = User.objects.create(name='Kim')
user2 = User.objects.create(name='Lee')
article1 = Article.objects.create(title='1글', user=user1)
article2 = Article.objects.create(title='2글', user=user1)
article3 = Article.objects.create(title='3글', user=user2)
c1 = Comment.objects.create(content='1글1댓글', user=user1, article=article1)
c2 = Comment.objects.create(content='1글2댓글', user=user2, article=article1)
c3 = Comment.objects.create(content='1글3댓글', user=user1, article=article1)
c4 = Comment.objects.create(content='1글4댓글', user=user2, article=article1)
c5 = Comment.objects.create(content='2글1댓글', user=user1, article=article2)
c6 = Comment.objects.create(content='!1글5댓글', user=user2, article=article1)
c7 = Comment.objects.create(content='!2글2댓글', user=user2, article=article2)





# 2번 댓글을 쓴 사람의 모든 게시글
c2.user.article_set.all()

# 1번 글의 첫번째 댓글/ 마지막 댓글을 쓴 사람의 이름
article1.comment_set.all[0].user.name
article1.comment_set.last().user.name

# 1번 글의 2번째부터 4번째까지 댓글을 가져오면?
article1.comment_set.all()[1:4]

# 1번 글의 첫번째 ~ 두번째 댓글을 가져오면?
article1.comment_set.all()[:2]

# 1번 글의 두번째 댓글을 쓴 사람의 첫번째 게시물의 작성자 이름
article1.comment_set.all()[1].user.article_set.all()[0].user.name

# 1번 댓글의 user 정보만 가져오면?
Comment.objects.values('user').all()

# 2번 사람이 작성한 댓글을 content 기준 내림차순으로 가져오면?
user2.comment_set.order_by('-content')

# 제목이 '1글' 인 게시글은?
 Article.objects.filter(title='1글')


```



## 참고

```
https://developer.mozilla.org/ko/docs/Learn/Server-side/Django
```

