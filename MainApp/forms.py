# from dataclasses import field
# from django import forms
# from .models import User
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