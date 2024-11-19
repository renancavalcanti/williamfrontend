from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('login/', views.get_login,name='login'),
    path('CreateAccount/', views.CreateAccount, name='CreateAccount')
]