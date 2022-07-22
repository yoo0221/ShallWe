from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def chat(request):
    return render(request, 'chat_index.html')

@login_required
def room(request, room_name):
    return render(request, 'chat_room.html', {'room_name':room_name})