# !/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
@Author: Longmin
@Time: 2020/3/3 10:50 下午
"""
from django.urls import path
from . import views


app_name = 'polls'  # 使用URLconf的命名空间，添加变量来指定该应用的命名空间
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/votes/
#     path('<int:question_id>/vote/', views.vote, name='vote')
# ]
"""将上面的代码修改为通用视图的方式，步骤：
    1. 修改URLconf设置
    2. 删除旧的无用视图
    3. 采用基于类视图的新视图

"""
urlpatterns = [
    path('', views.IndexView.as_view)
]