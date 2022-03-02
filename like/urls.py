from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.user_view, name='user-view'),
    path('main/like/<int:id>/', views.user_like, name='user-like'),
    path('main/hate/<int:id>/', views.user_hate, name='user-hate'),
]
