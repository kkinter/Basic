from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    _todos = Todo.objects.all()
    context = {
        "todos": _todos,
    }

    return render(request, "index.html", context)


def create(request):

    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    print(priority)
    # print(content)
    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    return redirect("todos:index")


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect("todos:index")


def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()

    return redirect("todos:index")
