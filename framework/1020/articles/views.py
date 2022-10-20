from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

from .forms import ArticleForm

@login_required
def create(request):
    user = request.user
    article_form = ArticleForm()
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = user
            article.save()
            return redirect('articles:index')
    context = {
        "article_form" : article_form,
    }
    return render(request, 'articles/form.html',context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : comments
    }
    return render(request, 'articles/detail.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article_form = ArticleForm(instance=article)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        article_form.save()
        return redirect('articles:index')
    context = {
        'article_form' : article_form,
    }
    return render(request, 'articles/form.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')

from .forms import CommentForm

@login_required
def comment_create(request, article_pk):
    user = request.user
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = user
        comment.save()
    
    return redirect('articles:detail', article.pk)

from .models import Comment
@login_required
def comment_delete(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == article.user:
        comment.delete()
    return redirect('articles:detail', article.pk)