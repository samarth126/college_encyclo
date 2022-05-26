from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('login/', views.loginr, name='loginr'),
    
]