from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.user_view, name='user-view'),
    path('main/follow/<int:id>/', views.user_follow, name='user-follow')
]