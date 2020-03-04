# !/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
@Author: Longmin
@Time: 2020/3/3 10:50 下午
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index')
]
