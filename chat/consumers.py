# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Message, Room

class ChatConsumer(WebsocketConsumer):
    # def save_message(self, data):
        

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope['user']

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        author = self.user
        message = data['message']
        room = Room.objects.get(pk=int(self.room_name))
        Message.objects.create(
            message=message,
            author=author,
            room=room
        )
        # save_message(self, text_data_json)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.user.username,
                'name': self.user.name
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        username = event['username']
        name = event['name']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'name': name
        }))