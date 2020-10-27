from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apitest.models import *

# Create your views here.


@login_required()
def welcome(request):
    return render(request, 'welcome.html')


def default(request):
    return HttpResponse("火星人~~ 欢迎来到地球！！😋")


# 返回子页面
def child(request, eid, oid=None):
    return render(request, eid)


@login_required
def home(request):
    return render(request, 'welcome.html', {"whichHTML": "Home.html", "oid": ""})


def login(request):
    pass
    return render(request, 'login.html')


def register(request):
    pass
    return render(request, 'register.html')


def tucao(request):
    tucao_text = request.GET['tucao_text']
    tucao.objects.create(user=request.user.username, text=tucao_text)
    return HttpResponse('')


def p_help(request):
    return render(request, 'welcome.html', {"whichHTML": "help.html", "oid": ""})


# 退出登录
def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect('/login/')


def login_action(request):
    username = request.GET['username']
    password = request.GET['password']
    print(username, password)

    from django.contrib import auth
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        request.session['user'] = username
        return HttpResponse('成功')
    else:
        return HttpResponse('失败')


def register_action(request):
    username = request.GET['username']
    password = request.GET['password']

    from django.contrib.auth.models import User
    try:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return HttpResponse('注册成功！')
    except:
        return HttpResponse('注册失败！用户似乎已经存在了呢~~')
