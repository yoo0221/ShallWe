from django.shortcuts import render, redirect
from django.contrib import auth
# Create your views here.
def register(request):
    return render(request, 'register.html')

def login(request):
    if (request.method == 'POST'):
        user_id = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=user_id, password=password)
        bad_login = 0
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            bad_login = 1
            return redirect('home', {'bad_login':bad_login})
            
    return render(request, 'login.html')

def home(request):
    return render(request, 'index.html')

