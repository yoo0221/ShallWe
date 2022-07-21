from django.shortcuts import get_object_or_404, render, redirect
from AccountApp.models import User
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request, 'index.html')

def search(request):
    result = User.objects.filter(is_superuser=False).order_by("-date_joined")
    return render(request, 'search.html', {"result":result})

def filtered(request):
    if request.method=="POST":
        f_age20 = request.POST['filter-age20']
        f_age30 = request.POST['filter-age30']
        f_age40 = request.POST['filter-age40']
        f_sex = request.POST['filter-sex']
        f_do = request.POST['addressDo']
        f_sgg = request.POST['addressSiGunGu']
        f_emd = request.POST['addressEMD']
        # 연령 필터
        result = User.objects.filter(is_superuser=False)
        age = User.objects.filter(sex='none')
        tempage = age
        if f_age20 == "20":
            age |= User.objects.filter(age__gt=18) & User.objects.filter(age__lt=29)
            # age |= Q(age__gt=18) & Q(age__lt=29)
        if f_age30 == "30":
            age |= User.objects.filter(age__gt=28) & User.objects.filter(age__lt=39)
        if f_age40 == "40":
            age |= User.objects.filter(age__gt=38)
            
        if age == tempage:
            age = sex=User.objects.filter()

        # 성별 필터, ok
        sex = None
        if f_sex == "남":
            sex=User.objects.filter(sex="남")
        elif f_sex == "여":
            sex=User.objects.filter(sex="여")

        if sex is None:
            sex = User.objects.filter()
        # 거주 지역 필터
        # 시/도
        result &= age & sex

        if f_do != "none":
            do = User.objects.filter(address_do=f_do)
            if f_sgg != "none":
                sgg = User.objects.filter(address_sgg=f_sgg)
                if f_emd != "none":
                    emd = User.objects.filter(address_emd=f_emd)
                    result &= do & sgg & emd
                else:
                    result &=do & sgg
            else:
                result &= do
        print(result)
        return render(request, 'search.html', {"result":result.order_by('-date_joined')})

def setprofile(request):
    return render(request, 'setprofile.html')

def themaselect(request):
    return render(request, 'themaselect.html')

def thema(request):
    return render(request, 'thema.html')

def promise(request):
    return render(request, 'promise.html')

def meet(request):
    return render(request, 'meet.html')