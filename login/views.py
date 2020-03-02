"""
路由转发用户请求到视图函数。视图函数处理用户请求，即编写业务处理逻辑，一般都在views.py文件中。
"""

from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models


# Create your views here.
# user_list = []


def index(request):  # 第一个参数必须是request，名字最好不要改，这是潜规则。request参数封装了用户请求的所有内容。
    # return HttpResponse("Hello, World!")  # 不能直接返回字符串，必须由这个类封装起来，才能被HTTP协议识别。
    # return render(request, 'index.html') render方法使用数据字典和请求元数据，渲染一个指定的HTML模板。其中多个参数中，第一个参数必须是request，第二个参数是模板。
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        # temp = {'usr': 'username', 'pwd': 'password'}
        # user_list.append(temp)
        # 将数据保存到数据库
        models.UserInfo.objects.create(usr=username, pwd=password)
    # 从数据库读取所有数据，注意缩进
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data': user_list})  # 用户列表作为上下文参数提供给render渲染index页面
