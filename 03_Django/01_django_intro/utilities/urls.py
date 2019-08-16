from django.urls import path
from . import views  # 현재 디렉토리에 있는 views를 import한다.

urlpatterns = [
    path('', views.index),
    path('mamago/', views.mamago),
    path('translated/', views.translated),
]