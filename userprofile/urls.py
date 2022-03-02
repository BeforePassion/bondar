from django.urls import path

from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path("image", views.image_profile, name="image_profile"),
]
