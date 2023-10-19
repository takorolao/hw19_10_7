from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('ice_cream/create/', views.create_ice_cream, name='create_ice_cream'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('form/', views.my_view, name='form'),
]
