from django.urls import path
from . import views

app_name='articles'

urlpatterns=[
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/',views.detail, name='detail'), #view.py의 detail함수 pk변수와 같은 이름
    path('<int:pk>/delete/',views.delete, name='delete'),
    path('<int:pk>/edit/',views.edit, name='edit'),
    path('<int:pk>/update/',views.update, name='update'),
]