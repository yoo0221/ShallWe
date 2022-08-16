from django.shortcuts import render
from .models import Room
# Create your views here.
def index(request):
    return render(request, 'chat_index.html')

def room(request, room_name):
    return render(request, 'chat_room.html', {
        'room': Room.objects.get(id=room_name),
        'user': request.user
    })