from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<article_pk>', views.detail, name='detail'),
    path('update/<article_pk>', views.update, name='update'),
    path('delete/<article_pk>', views.delete, name='delete'),
    path('comment_create/<article_pk>', views.comment_create, name='comment_create'),
    path('comment_delete/<article_pk>/<comment_pk>/', views.comment_delete, name='comment_delete'),
] 