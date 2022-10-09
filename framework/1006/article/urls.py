from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("delete/<int:pk>", views.delete, name="delete-review"),
    path("update/<int:pk>", views.update, name="update-review"),
    path("detail/<int:pk>", views.detail, name="detail-review"),
]
