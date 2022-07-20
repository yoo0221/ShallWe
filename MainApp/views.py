from django.shortcuts import get_object_or_404, render, redirect
from AccountApp.models import User
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request, 'index.html')

def search(request):
    if request.method=="POST":
        f_age20 = int(request.POST['filter-age20'])
        f_age30 = int(request.POST['filter-age30'])
        f_age40 = int(request.POST['filter-age30'])
        f_sex = request.POST['filter-sex']
        f_do = request.POST['addressDo']
        f_sgg = request.POST['addressSiGunGu']
        f_emd = request.POST['addressEMD']
        # 연령 필터
        age = None
        if f_age20 == "20":
            age = User.objects.filter(age__gt=18) & User.objects.filter(age__lt=29)
        if f_age30 == "30":
            age |= User.objects.filter(age__gt=28) & User.objects.filter(age__lt=39)
        if f_age40 == "40":
            age |= User.objects.filter(age__gt=38)
            
        if age is None:
            age = sex=User.objects.filter()
        # 성별 필터
        sex = None
        if f_sex == "남":
            sex=User.objects.filter(sex="남")
        elif f_sex == "여":
            sex=User.objects.filter(sex="여")

        if sex is None:
            age = sex=User.objects.filter()
        # 거주 지역 필터
        # 시/도
        if f_emd != "none":
            emd = User.objects.filter(address_emd=f_emd)
            if f_sgg != "none":
                sgg = User.objects.filter(address_sgg=f_sgg)
                if f_do != "none":
                    do = User.objects.filter(address_do=f_do)
                    location = emd&sgg&do
                else:
                    location = emd&sgg
            else:
                location = emd
            result = age & sex & location
        else:
            result = age & sex
    else:
        result = User.objects.filter().order_by("-date_joined")
        print(result)
        
    return render(request, 'search.html', {"result":result})

def setprofile(request):
    return render(request, 'setprofile.html')

def themaselect(request):
    return render(request, 'themaselect.html')

def thema(request):
    return render(request, 'thema.html')

def promise(request):
    return render(request, 'promise.html')