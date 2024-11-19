from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('main/', views.main_view, name='main'),  # Define the main view here
    path('Disconnect',views.Disconnect,name='Disconnect'),
   
    path('send-task/', views.Create_Task, name='Create_Task'),
    path('task-assigned/', views.Task_Assigned, name='task_assigned'),
    path('task-sent/', views.task_sent, name='task_sent'),
    path('task-update/<str:taskUid>', views.task_updated, name='updated'),
    path('task-delete/<str:taskUid>', views.task_deleted, name='deleted'),
]
