# !/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
@Author: Longmin
@Time: 2020/10/13 10:18 上午
"""
from django import forms
from captcha.fields import CaptchaField
from captcha.fields import CaptchaTextInput

""" Django表单功能：
	1. 准备和重构数据用于页面渲染
	2. 为数据创建HTML表单元素
	3. 接收和处理用户从表单发送过来的数据
"""


class UserForm(forms.Form):
	username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': '用户名',
		'autofocus': ''
	}))
	password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={
		'class': 'form-control',
		'placeholder': '密码'
	}))
	captcha = CaptchaField(label='验证码', widget=CaptchaTextInput(attrs={
		'class': 'form-control',
		'placeholder': '请输入验证码'
	}))


class RegisterForm(forms.Form):
	gender = (
		('male', '男'),
		('female', '女'),
	)
	username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': '用户名'
	}))
	password1 = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={
		'class': 'form-control',
		'placeholder': '密码'
	}))
	password2 = forms.CharField(label='确认密码', max_length=256, widget=forms.PasswordInput(attrs={
		'class': 'form-control',
		'placeholder': '确认密码'
	}))
	email = forms.EmailField(label='邮箱地址', widget=forms.EmailInput(attrs={
		'class': 'form-control',
		'placeholder': '邮箱地址'
	}))
	sex = forms.ChoiceField(label='性别', choices=gender, initial='male', widget=forms.Select(attrs={
		'class': 'form-control'
	}))
	captcha = CaptchaField(label='验证码', widget=CaptchaTextInput(attrs={
		'class': 'form-control',
		'placeholder': '请输入验证码'
	}))
