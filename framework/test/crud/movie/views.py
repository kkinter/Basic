from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {"reviews": reviews}
    return render(request, "movie/index.html", context)


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    Review.objects.create(title=title, content=content)
    return redirect("movie:index")


def detail(requset, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }

    return render(requset, "movie/detail.html", context)


def new(request):
    return render(request, "movie/new.html")


def delete(request, pk):
    del_review = Review.objects.get(pk=pk)
    del_review.delete()

    return redirect("movie:index")


def edit(request, pk):
    review = Review.objects.get(pk=pk)
    context = {"review": review}

    return render(request, "movie/edit.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)
    title = request.GET.get("edit-title")
    content = request.GET.get("edit-content")
    review.title = title
    review.content = content
    review.save()

    return redirect("movie:index")
