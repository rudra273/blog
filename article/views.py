from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required 

from django.views.generic.edit import UpdateView, DeleteView

from django.urls import reverse_lazy

# Create your views here.

#conetxt processor - category
def categories(request): 

    categories = Category.objects.all()

    return {
        'categories': categories,
    }


def search_article(request):

    if 'query' in request.GET:
        query = request.GET['query'] 
        articles = Article.objects.filter(title__icontains=query) | Article.objects.filter(content__icontains=query)

    context = {
        'articles': articles,
        'query' : query,
    } 

    return render(request, 'article/categorised_article.html', context)


def index(request):
     
    all_articles = Article.objects.all()

    recent_articles = Article.objects.all().order_by('pub_date')[:3] 

    context = {
        'articles': all_articles,

        'recent_articles': recent_articles
    }

    return render(request, 'article/index.html', context) 


def single_article(request, pk):

    article = Article.objects.get(pk=pk)

    context = {
        "article": article,  
    }

    return render(request, 'article/article.html', context)


def categorised_article(request, pk):

    if pk == 0:
        articles = Article.objects.all()
        context = {
            'articles': articles, 
            'category' : 'all' 
            } 

    else:
        category = Category.objects.get(pk=pk)
        articles = Article.objects.filter(category = category).all()

        context ={
            'articles': articles,
            'category' : category, 
        }

    return render(request, 'article/categorised_article.html', context)   

@login_required
def post_article(request):  
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)  
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()  
            return redirect('article:single_article', pk=form.instance.id) 

    context = { 
        'form' : form
    } 
    return render(request, 'article/article_form.html', context) 


# class UpdateArticle(UpdateView):
#     model = Article

#     fields = ["category", "title", "img", "content"] 

#     template_name_suffix = "_update" 

class UpdateArticle(UpdateView):

    model = Article

    form_class = ArticleForm

    template_name_suffix = "_update"

class DeleteArticle(DeleteView):

    model = Article 

    success_url = reverse_lazy('users:profile') 


