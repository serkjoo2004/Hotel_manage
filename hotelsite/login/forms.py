from django import forms
from .models import Guest

class UserForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = [
            'guest_id', 
            'guest_pw', 
            'first_name', 
            'last_name', 
            'date_of_birth',
            'sex',
            'phone_num',
            'e_mail',
            'language',
            ]
        labels ={
            'guest_id':'아이디', 
            'guest_pw':'비밀번호', 
            'first_name':'이름', 
            'last_name':'성', 
            'date_of_birth':'생년월일',
            'sex':'성별',
            'phone_num':'휴대전화번호',
            'e_mail':'e_mail',
            'language':'선호 언어',
        }