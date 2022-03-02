from django.urls import path
from .views import VerificationView

from . import views

urlpatterns = [
    # path("", views.test, name="test"),
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>', views.VerificationView.as_view(), name='activate'),
    path('', views.startpage, name='startpage'),
]
