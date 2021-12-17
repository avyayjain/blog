from django.urls import path
from blog_app import views

urlpatterns = [
    path('',views.Home,name = 'home'),
    path('register',views.Register,name = 'register'),
    path('login',views.login,name='login'),
    path('logout',views.LogOut,name='logout'),
    path('search',views.search,name='search'),
    path('about',views.About,name='about')
]