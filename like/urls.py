from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.user_view, name='user-view'),
    path('main/like/<int:id>/', views.user_like, name='user-like'),
    path('like-me/like2/<int:id>/', views.user_like2, name='user-like2'),
    path('main/hate/<int:id>/', views.user_hate, name='user-hate'),
    path('like-me/hate2/<int:id>/', views.user_hate2, name='user-hate2'),
]
