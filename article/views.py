from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
     
    all_articles = Article.objects.all()

    context = {
        'articles': all_articles,
    }

    return render(request, 'article/index.html', context) 


