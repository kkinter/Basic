from django.shortcuts import render, redirect
from .models import Review

## forms
from .forms import ReviewForm

# Create your views here.
def index(request):
    reviewObj = Review.objects.all()
    context = {
        "reviews": reviewObj,
    }
    return render(request, "article/index.html", context)


def new(request):
    return render(request, "article/new.html")


def create(request):
    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("article:index")

    context = {"form": form}

    return render(request, "article/new.html", context)


def delete(request, pk):
    review = Review.objects.get(pk=pk)

    if request.method == "POST":
        review.delete()
        return redirect("article:index")

    context = {"object": review}
    return render(request, "article/delete.html", context)


def update(request, pk):
    project = Review.objects.get(id=pk)
    form = ReviewForm(instance=project)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("article:index")

    context = {"form": form}
    return render(request, "article/new.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "article/detail.html", context)
