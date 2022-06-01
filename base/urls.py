from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('login/', views.loginr, name='loginr'),
    path('events/', views.events, name='events'),
    path('notices/', views.notices, name='notices'),
    path('notes/', views.notes, name='notes'),
    path('qps/', views.qps, name='qps'),
    path('opd/', views.opd, name='opd'),
    
]