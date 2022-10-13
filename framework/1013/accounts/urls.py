from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('<int:user_pk>', views.detail, name='detail'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/password/', views.update_password, name='update_password'),
    path('delete/', views.delete, name='delete'),
]

