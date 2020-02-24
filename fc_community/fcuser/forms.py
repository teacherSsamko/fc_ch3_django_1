from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="사용자 이름")
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
