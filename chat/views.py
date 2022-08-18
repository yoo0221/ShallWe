from http.client import HTTPResponse
from django.shortcuts import render
from .models import Room, Message
# Create your views here.
def index(request):
    return render(request, 'chat_index.html')

def room(request, room_name):
    room = Room.objects.get(id=room_name)
    messages = room.messages.all()
    if request.user != room.user1 and request.user != room.user2:
        return render(request, 'error.html')
    else:    
        return render(request, 'chat_room.html', {
            'room': room,
            'messages': messages,
            'user': request.user
        })