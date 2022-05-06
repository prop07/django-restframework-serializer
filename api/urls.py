from django.urls import path
from . import views


urlpatterns = [
    path('',views.apiview,name='api-view'),
    path('todo-list/',views.todoList,name='todo-list'),
    path('todo-list/<str:pk>/',views.tododetail,name='todo-detail'),
    path('todo-create/',views.todoCreate,name='todo-create'),
    path('todo-update/<str:pk>/',views.todoUpdate,name='todo-Update'),
    path('todo-delete/<str:pk>/',views.todoDelete,name='todo-delet'),





]