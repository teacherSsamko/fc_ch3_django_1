from django.shortcuts import render
from .models import Fcuser
from django.http import HttpResponse

# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']

        res_data = {}
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            fcuser = Fcuser(
                username=username,
                password=password,
            )

            fcuser.save()

        return render(request, 'register.html', res_data)
