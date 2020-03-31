from django.urls import path
from . import views

urlpatterns=[
    path('static_example/', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/',views.result),
    path('art/',views.art),
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('lotto/', views.lotto),
    path('ispal/<pal>/', views.ispal),
    path('isbirth/<my_birth>', views.isbirth),
    path('template_language/', views.template_language),
    path('circle/<int:r>/', views.circle),
    path('mul/<int:num1>/<int:num2>/', views.mul),
    path('introduce2/<name>/<int:age>/', views.introduce2),
    path('hello/<name>/<int:age>/', views.hello), #type의 default는 str
    path('lorempic/', views.lorempic),
    path('dinner/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
]


    