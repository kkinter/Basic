from turtle import title
from django.shortcuts import render, redirect
from .models import Review
# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    Review.objects.create(
        title = title,
        content = content,
    )
    return redirect('articles:index')

def detail(request, pk):
    review = Review.objects.get(pk = pk)
    context = {
        'review':review
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    del_review = Review.objects.get(pk=pk)
    del_review.delete()

    return redirect('articles:index')