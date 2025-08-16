from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
]