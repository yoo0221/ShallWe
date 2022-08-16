# chat/urls.py
from django.urls import path
from chat import views

urlpatterns = [
    path('', views.index, name='chat'),
    path('<str:room_name>/', views.room, name='room'),
]