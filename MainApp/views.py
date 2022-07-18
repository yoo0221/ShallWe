from django.shortcuts import render, redirect
from django.contrib import auth
# Create your views here.
def register(request):
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

def home(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def setprofile(request):
    return render(request, 'setprofile.html')

