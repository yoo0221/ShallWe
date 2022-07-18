from django.shortcuts import render, redirect
from .models import User 
from django.contrib import auth
# Create your views here.
def register(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        if (User.objects.get(username=username) == None) and (request.POST['password'] == request.POST['repeat']):
            new_user = User.objects.create_user(username=username,
                                                password=request.POST['password'],
                                                email=request.POST['email'],
                                                name=request.POST['name'],
                                                birth=request.POST['birth'],
                                                residence=request.POST['residence'],
                                                sex=request.POST['sex'],
                                                nationality=request.POST['nationality'],
                                                mother_tongue=request.POST['mother_tongue'])
            auth.login(request, new_user)
            return redirect('home')
        else:
            pass
    return render(request, 'register.html')

def login(request):
    bad_login = False
    if (request.method == 'POST'):
        user_id = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=user_id, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            bad_login = True
            return render(request, 'login.html', {'bad_login':bad_login})
    return render(request, 'login.html', {'bad_login':bad_login})