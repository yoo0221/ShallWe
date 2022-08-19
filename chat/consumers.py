# chat/consumers.py
import json, datetime
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
        message_text = data['message']
        author = self.user
        room = Room.objects.get(pk=int(self.room_name))
        sort = data['sort']
        if sort == "ordinary":
            Message.objects.create(
                message=message_text,
                author=author,
                room=room,
                sort=sort
            )
        elif sort == "thema":
            Message.objects.create(
                message=message_text,
                author=author,
                room=room,
                sort=sort,
                thema_sort="유행",
                thema_num=1,
                thema_confirmed=False
            )
        elif sort == "promise":
            Message.objects.create(
                message=message_text,
                author=author,
                room=room,
                sort=sort,
                promise_place="그린빈 카페",
                promise_address="서울특별시",
                promise_time=datetime.datetime.now(),
                promise_confirmed=False
            )

        # dict = {}
        # dict['message']=message.message
        # dict['author']=message.author
        # dict['created_time']=message.created_time
        # dict['room']=message.room
        # dict['sort']=message.sort
        # dict['thema_sort']=message.thema_sort
        # dict['thema_num']=message.thema_num
        # dict['thema_confirmed']=message.thema_confirmed
        # dict['promise_place']=message.promise_place
        # dict['promise_address']=message.promise_address
        # dict['promise_time']=message.promise_time
        # dict['promise_confirmed']=message.promise_confirmed

        # message = dict
        # save_message(self, text_data_json)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_text,
                'username': self.user.username,
                'name': self.user.name,
                'sort': sort,
                'thema_sort':"유행",
                'thema_num':1,
                'thema_confirmed':False,
                'promise_place':'그린빈 카페 냉천점',
                'promise_time':"2022-08-20 토요일  오후 2:00",
            }
        )
    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        username = event['username']
        name = event['name']
        sort = event['sort']
        thema_sort = event['thema_sort']
        thema_num = event['thema_num']
        thema_confirmed = event['thema_confirmed']
        promise_place = event['promise_place']
        promise_time = event['promise_time']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'name': name,
            'sort': sort,
            'thema_sort': thema_sort,
            'thema_num': thema_num,
            'thema_confirmed': thema_confirmed,
            'promise_place': promise_place,
            'promise_time': promise_time,
        }))