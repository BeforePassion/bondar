"""
When Django accepts an HTTP request, it consults the root URLconf to lookup a view function,
and then calls the view function to handle the request. Similarly, when Channels accepts a WebSocket connection,
it consults the root routing configuration to lookup a consumer,
and then calls various functions on the consumer to handle events from the connection.
"""
# websocket 요청을 처리하는 함수는 consumers.py 에입력
import json

from channels.generic.websocket import AsyncWebsocketConsumer


# 비동기식 방법으로 진행
class ChatConsumer(AsyncWebsocketConsumer):
    # websocket 연결
    async def connect(self):
        # room_name 파라미터를 chat/routing.py URl 에서 얻고, 열러있는 websocket에 접속
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # 인용이나 이스케이프 없이 사용자 지정 방 이름에서 직접 채널 그룹 이름을 구성
        # 그룹 이름에는 문자, 숫자, 하이픈 및 마침표만 사용할 수 있어서 튜토리얼 예제 코드는 다른 문자가 있는 방이름 에서는 실패
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group / 그룹에 참여
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        # websocket 연결을 수락 / connect() 메서드 내에서 accept()를 호출하지 않으면 연결이 거부되고 닫힌다.
        await self.accept()

    # websocket 연결 해제
    async def disconnect(self, close_code):
        # Leave room group / 그룹에서 탈퇴
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = text_data_json["user"]

        # Send message to room group / 그룹에 이벤트를 보낸다.
        # An event has a special 'type' key corresponding to the name of the method
        # that should be invoked on consumers that receive the event.
        await self.channel_layer.group_send(self.room_group_name, {"type": "chat_message", "message": message, "user": user})

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
