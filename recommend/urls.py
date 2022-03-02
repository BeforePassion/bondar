from django.urls import path

from . import views

urlpatterns = [
    path('i-like/', views.i_like_user_view, name='i_like'),
    path('i-hate/', views.hate_user_view, name='i_hate'),
    path('like-me/', views.like_me_user_view, name='like_me'),
    path('both-like/', views.both_like_user_view, name='both_like'),
    path('i-like/unlike/<int:id>', views.user_unlike, name='user_unlike'),
    path('i-hate/cancel/<int:id>', views.hate_cancel, name='hate_cancel')
]