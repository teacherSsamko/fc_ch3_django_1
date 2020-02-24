from django.shortcuts import render, redirect
from .models import Fcuser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)
    return HttpResponse('HOME!')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        else:
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
                # login process
                # Session
                # session에 fcuser.id(pk)를 저장
                request.session['user'] = fcuser.id
                # Redirect
                return redirect('/')

            else:
                res_data['error'] = '비밀번호가 틀립니다.'

        return render(request, 'login.html', res_data)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        # get method -> 입력값 없이 제출해도 오류를 발생시키지 않음
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        useremail = request.POST.get('useremail', None)

        res_data = {}

        if not (username and password and re_password and useremail):
            res_data['error'] = '모든 값을 입력해야합니다.'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            fcuser = Fcuser(
                username=username,
                password=make_password(password),
                useremail=useremail,
            )

            fcuser.save()

        return render(request, 'register.html', res_data)
