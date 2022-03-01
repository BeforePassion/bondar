from django.urls import path

from . import views

urlpatterns = [
    path('ilike/', views.ilike, name='ilike'),
    # path('likeme/', views.likeme, name='likeme'),
]