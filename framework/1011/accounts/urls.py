from django.urls import path
from . import views
import accounts

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('detail/<int:pk>', views.detail, name="detail"),
]
