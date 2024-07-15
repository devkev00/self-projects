from django.urls import path, include
from .views import *

app_name = 'todolist'

urlpatterns = [
    path('', todolist_home, name='todolist_home'),
    path('create', todolist_create, name='todolist_create'),
    path('delete/<int:pk>/', todolist_delete, name='todolist_delete'),
    path('update/<int:pk>/', todolist_update, name='todolist_update'),
]