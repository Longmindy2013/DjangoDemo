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
def child(request, eid, oid):
    res = child_json(eid, oid)
    return render(request, eid, res)


# 控制不同的页面返回不同的数据：数据分发器
def child_json(eid, oid=''):
    res = {}
    if eid == 'Home.html':
        date = home_link.objects.all()
        res = {"links": date}
    elif eid == 'project_list.html':
        date = project.objects.all()
        res = {"projects": date}
    elif eid == 'api_library.html':
        project_name = project.objects.filter(id=oid)[0]
        res = {"project_name": project_name}
    return res


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


def project_list(request):
    pass
    return render(request, 'welcome.html', {"whichHTML": "project_list.html", "oid": ""})


def delete_project(request):
    project_id = request.GET['id']
    project.objects.filter(id=project_id).delete()
    return HttpResponse('')


def add_project(request):
    project_name = request.GET['project_name']
    project.objects.create(project_name=project_name, project_remark='', project_build_user=request.user.username, project_build_other_user='')
    return HttpResponse('')


def to_apis_library(request, id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML": "api_library.html", "oid": project_id})


def to_cases_library(request, id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML": "case_library.html", "oid": ""})


def to_project_settings(request, id):
    project_id = id
    return render(request, 'welcome.html', {"whichHTML": "project_settings.html", "oid": ""})
