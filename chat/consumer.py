# websocket 요청을 처리하는 함수는 consumers.py 에입력
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Room, Message

from AccountApp.models import User
from MainApp.models import UserProfile

class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        room_id = int(self.room_name)
        messages = Message.last_30_messages(self, room_id=room_id)
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        user_id = data['user_id']
        room_id = int(self.room_name)
        user_contact = User.objects.filter(id=user_id)[0]
        room_contact = Room.objects.filter(id=room_id)[0]
        message_creat = Message.objects.create(
            user_id=user_contact,
            room_id=room_contact,
            message=data['message']
        )
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message_creat)
        }
        return self.send_chat_message(content)

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'author': message.user_id.username,
            'content': message.message,
            'timestamp': str(message.created_at)
        }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope['user']

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

    # websocket 연결 해제
    def disconnect(self, close_code):
        # Leave room group / 그룹에서 탈퇴
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps(message))