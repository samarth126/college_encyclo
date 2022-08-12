from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [

    path('',views.home, name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('logins/', views.logins, name='logins'),
    path('events/', views.events, name='events'),
    path('events_self/', views.events_self, name='events_self'),
    path('events_other/', views.events_other, name='events_other'),
    path('notices/', views.notices, name='notices'),
    path('notes/', views.notes, name='notes'),
    path('subnotes/<int:pk>/', views.subnotes, name='subnotes'),
    path('qps/', views.qps, name='qps'),
    path('opd/', views.opd, name='opd'),
    path('proform/', views.proform, name='proform'),
    path('staffproform/', views.staffproform, name='staffproform'),
    # path('login/', views.loginr, name='loginr'),
    
]