from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    article_form = ArticleForm()
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    context = {
        'article_form' : article_form
    }

    return render(request, 'articles/form.html', context)
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article_form = ArticleForm(instance=article)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    context = {
        'article_form' : article_form, 
    }
    return render(request, 'articles/form.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment_form.save()
    return redirect('articles:detail', article.pk)
    
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
