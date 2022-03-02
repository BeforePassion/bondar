from django.urls import path

from chat import views

urlpatterns = [
    path("", views.chat_view, name="chat"),  # /chat/으로 넘어오면 chat_view 함수 실행
    path("<str:room_name>/", views.room_view, name="room"),  # /chat/room_number/ 으로 넘어오면 room 함수 실행
    path("api/<int:user_id>", views.api_create_room, name="api_create_room"),
]
