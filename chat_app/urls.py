from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("chat/", views.chat, name="chat"),
    path("chat2/", views.chat2, name="chat2"),
]