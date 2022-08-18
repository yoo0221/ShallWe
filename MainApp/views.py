from cProfile import Profile
from django.shortcuts import get_object_or_404, render, redirect
from AccountApp.models import User
from MainApp.models import UserProfile
from django.db.models import Q
from MainApp.forms import SetProfileForm, SetScheduleForm
from django.contrib.auth.decorators import login_required
from chat.models import Room, Message, Thema, ThemaMessage

# Create your views here.

@login_required
def home(request):
    users = User.objects.filter(is_superuser=False).order_by('-date_joined')
    users = users.exclude(username=request.user)
    return render(request, 'index.html', {"users":users})

@login_required
def search(request):
    result = User.objects.filter(is_superuser=False).order_by("-date_joined")
    return render(request, 'search.html', {"result":result})

@login_required
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
        return render(request, 'search.html', {"result":result.order_by('-date_joined'),"count":len(result)})

# def setprofile(request):
#     if request.method == 'POST' or request.method == 'FILES':
#         user = get_object_or_404(User, username=request.POST['user'])
#         # user.profile_photo = request.FILES['photo_img']
#         handle_uploaded_file(request.FILES['file'])
#         user.skill = request.POST['skill']
#         user.introduction = request.POST['introduction']
#         user.interesting_keyword = request.POST['interesting_keyword']
#         user.like_place = request.POST['likeplace']
#         user.unlike_place = request.POST['unlikeplace']
#         user.save()
#     return render(request, 'setprofile.html')

@login_required
def setprofile(request):
    if request.method == "POST" or request.method == "FILES":
        filled_form = SetProfileForm(request.POST, request.FILES)
        try:
            user_profile = get_object_or_404(UserProfile, user=get_object_or_404(User, username=request.user))
        except:
            if filled_form.is_valid():
                final_form = filled_form.save(commit=False)
                final_form.user = get_object_or_404(User, username=request.user)
                final_form.save()
                return redirect('setprofile')
        
       
        if filled_form.is_valid():
            photo = filled_form.cleaned_data['photo']
            skill = filled_form.cleaned_data['skill']
            introduction = filled_form.cleaned_data['introduction']
            interesting_keyword = filled_form.cleaned_data['interesting_keyword']
            like_place = filled_form.cleaned_data['like_place']
            unlike_place = filled_form.cleaned_data['unlike_place']

            user = User.objects.get(username=request.user)
            user_profile = UserProfile.objects.get(user=user)

            if photo is None:
                photo = user_profile.photo
            if skill is None:
                skill = user_profile.skill
            if introduction is None:
                introduction = user_profile.introduction
            if interesting_keyword is None:
                interesting_keyword = user_profile.interesting_keyword
            if like_place is None:
                like_place = user_profile.like_place
            if unlike_place is None:
                unlike_place = user_profile.unlike_place

            user_profile.delete()
            final_form = filled_form.save(commit=False)
            final_form.user = get_object_or_404(User, username=request.user)
            final_form.save()
            return redirect('setprofile')
    else:
        form = SetProfileForm()
    return render(request, 'setprofile.html', {"form":form})

@login_required
def themaselect(request):
    if request.method == "POST":
        form = SetScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'promise.html')
    else:
        form = SetScheduleForm()
    return render(request, 'themaselect.html', {"form":form})

def hasRoom(user1, user2):
    room = Room.objects.filter(user1=User.objects.get(pk=user1))
    room = room.filter(user2=User.objects.get(pk=user2))
    room2 = Room.objects.filter(user2=User.objects.get(pk=user1))
    room2 = room.filter(user1=User.objects.get(pk=user2))
    room = room.union(room2)
    return room

@login_required
def thema(request, user_id):
    room = hasRoom(user_id, request.user.id)
    opponent = User.objects.get(pk=user_id)
    messages = room[0].messages.all()
    if request.method == 'POST':
        message="깻잎 논쟁을 아시나요?"
        author=request.user
        room=room[0]
        sort="thema"
        thema_sort="유행"
        number=1
        confirmed=False
        thema_msg=ThemaMessage.objects.create(
            message=message, author=author, room=room, sort=sort, thema_sort=thema_sort, number=number, confirmed=confirmed
        )
        return render(request, 'room.html', {"room":room[0], "messages":messages, 'user': request.user, 'opponent': opponent })
    else:
        return render(request, 'thema.html',{"room":room[0], "opponent":opponent})



@login_required
def themaafter(request, user_id):
    # print(request.user.id)
    room = hasRoom(user_id, request.user.id)
    if room.count() == 0:
        newroom = Room.objects.create(user1=User.objects.get(pk=user_id), user2=User.objects.get(pk=request.user.id))
        room_id = newroom.id
    else:
        room_id = room[0].id
    return redirect('room', str(room_id))

@login_required
def promise(request):
    return render(request, 'promise.html')

@login_required
def promise2(request):
    return render(request, 'promise2.html')

@login_required
def meet(request):
    return render(request, 'meet.html')

@login_required
def thema2(request):
    return render(request, 'thema2.html')

@login_required
def detail_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'detailProfile.html', {'user':user, 'profile':user_profile})

@login_required
def special_thema(request):
    return render(request, 'specialThema.html')

@login_required
def chat(request):
    return render(request, 'chat.html')

@login_required
def remind(request):
    return render(request, 'remind.html')

@login_required
def preview(request):
    return render(request, 'preview.html')

@login_required
def chat_ready(request, user_id):
    # print(request.user.id)
    room = hasRoom(user_id, request.user.id)
    if room.count() == 0:
        newroom = Room.objects.create(user1=User.objects.get(pk=user_id), user2=User.objects.get(pk=request.user.id))
        room_id = newroom.id
    else:
        room_id = room[0].id
    
    return redirect('room', str(room_id))
# def handle_uploaded_file(f):
#     with open(settings.MEDIA_ROOT+"/profile", 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def index(request):
    return render(request, 'index_temp.html')

def chatlist(request):
    rooms1 = Room.objects.filter(user1=request.user)
    rooms2 = Room.objects.filter(user2=request.user)
    rooms = rooms1.union(rooms2)
    return render(request, 'chatlist.html', {"rooms":rooms, "user":request.user})

def confirm(request):
    return render(request, 'confirm.html')