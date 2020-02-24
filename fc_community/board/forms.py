from django import forms
from django.contrib.auth.hashers import check_password


class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        }, max_length=128, label="제목")
    contents = forms.CharField(error_messages={
        'required': '내용을 입력해주세요.'
    }, label="내용", widget=forms.Textarea)
