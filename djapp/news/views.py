from django.shortcuts import render, get_object_or_404
from .models import Articles

def news_home(request):
    articles = Articles.objects.order_by('-data')  # новые сначала
    return render(request, 'news/news_home.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    return render(request, 'news/article_detail.html', {'article': article})