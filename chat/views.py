from http.client import HTTPResponse
from django.shortcuts import render
from .models import Room
# Create your views here.
def index(request):
    return render(request, 'chat_index.html')

def room(request, room_name):
    room = Room.objects.get(id=room_name)
    if request.user != room.user1 and request.user != room.user2:
        return render(request, 'error.html')
    else:    
        return render(request, 'chat_room.html', {
            'room': Room.objects.get(id=room_name),
            'user': request.user
        })