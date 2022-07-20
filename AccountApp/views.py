from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from .models import User 
from django.contrib import auth
from datetime import datetime

# Create your views here.
def register(request):
    overlapped = None
    if (request.method == 'POST'):
        username = request.POST['username']
        list1 = []
        list1.append(request.POST['birth-year'])
        list1.append(request.POST['birth-month'])
        list1.append(request.POST['birth-day'])
        birth_join='-'.join(list1)
        birth=datetime.strptime(birth_join, "%Y-%m-%d")

        age = (int(timezone.now().strftime("%Y%m%d"))-int(birth.strftime("%Y%m%d"))) / 10000
        
        overlapped = User.objects.filter(username=username)
        # if (overlapped == None) and (request.POST['password'] == request.POST['repeat']):

        if (request.POST['password'] == request.POST['repeat']):    
            user = User.objects.create_user(username=username,
                                            password=request.POST['password'],
                                            email=request.POST['email'],
                                            name=request.POST['name'],
                                            birth=birth,
                                            age=age,
                                            address_do=request.POST['addressDo'],
                                            address_sgg=request.POST['addressSiGunGu'],
                                            address_emd=request.POST['addressEMD'],
                                            sex=request.POST['sex'],
                                            nationality=request.POST['nationality'],
                                            mother_tongue=request.POST['mother_tongue'])
            auth.login(request, user)
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

def logout(request):
    auth.logout(request)
    return redirect('home')