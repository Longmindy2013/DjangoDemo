# !/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
@Author: Longmin
@Time: 2020/3/3 10:50 下午
"""
from django.urls import path
from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/votes/
    path('<int:question_id>/vote/', views.vote, name='vote')
]
