# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.user_follow, name='user-follow')
]