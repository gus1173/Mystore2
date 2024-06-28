
from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path("Home",views.HomeView.as_view(),name='acchome'),
    path("login",views.LoginView.as_view(),name='login'),
    path("register",views.RegisterView.as_view(),name='register'),
    path("",views.HomeView.as_view(),name='index'),
    path("Logout",views.lgout,name='logout')
]