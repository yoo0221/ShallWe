from django import forms
from MainApp.models import Profile

class SetProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'photo',
            'skill',
            'introduction',
            'interesting_keyword',
            'like_place',
            'unlike_place'
        )
        labels = {
            'photo': '',
            'skill': '언어 수준',
            'introduction':'본인 소개',
            'interesting_keyword':'관련 해시태그',
            'like_place':'이런 장소가 좋아요',
            'unlike_place':'이런 장소는 곤란해요'
        }
        
    def __init__(self, *args, **kwargs):
        super(SetProfileForm, self).__init__(*args, **kwargs)
        
        self.fields['photo'].widget.attrs = {
            # 'placeholder': '',
            'id':'photo_img',
            'class':'account-file-input',
            'hidden':'',
            'accept':"image/png, image/jpeg"
        }

        self.fields['skill'].widget.attrs = {
            'placeholder': '외국어 공부 경험, 외국 거주 경험 등',
            'id':'skill',
            'class':'form-control'
        }
        
        self.fields['introduction'].widget.attrs = {
            'placeholder': '나를 소개하는 한 줄',
            'id':'introduction',
            'class':'form-control',
            'value':''
        }

        self.fields['interesting_keyword'].widget.attrs = {
            'placeholder': '#MBTI #강아지 #먹방 #여행',
            'id':'interesting_keyword',
            'class':'form-control'
        }

        self.fields['like_place'].widget.attrs = {
            'placeholder': '카페가 특히 편해요, 딱히 없어요 등등',
            'id':'likeplace',
            'class':'form-control'
        }

        self.fields['unlike_place'].widget.attrs = {
            'placeholder': '이런 곳만 아니면 괜찮아요',
            'id':'unlikeplace',
            'class':'form-control'
        }
            # self.fields['skill'].label.attrs={

            # }
# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields=[
#                 'name',
#                 'email',
#                 'username', 
#                 'password', 
#                 'age', 
#                 'residence', 
#                 'sex', 
#                 'nationality',
#                 'mother_tongue'
#                 ]

#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)

#         self.fields['name'].widget.attrs = {
#             'class': 'form-control',
#             'placeholder': 'ex) 홍길동',
#             'id':'name',
#         }