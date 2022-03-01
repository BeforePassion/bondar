from django.urls import path

from . import views

urlpatterns = [
    path('i-like/', views.i_like_user_view, name='i_like'),
    path('like-me/', views.like_me_user_view, name='like_me'),
    path('i-like/unlike/<int:id>', views.user_unlike, name='user-unlike')
]