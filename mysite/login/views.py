from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms

# Create your views here.


def index(request):
	if not request.session.get('is_login', None):
		return redirect('/login/')
	return render(request, 'login/index.html')


def login(request):
	if request.session.get('is_login', None):
		return redirect('/index/')
	if request.method == 'POST':
		# username = request.POST.get('username')
		# password = request.POST.get('password')
		login_form = forms.UserForm(request.POST)
		message = '请核对填写的内容'
		# if username.strip() and password:
		if login_form.is_valid():
			username = login_form.cleaned_data.get('username')
			password = login_form.cleaned_data.get('password')
			captcha = login_form.cleaned_data.get('captcha')
			try:
				user = models.User.objects.get(name=username)
			except:
				# message = '用户不存在'
				return render(request, 'login/login.html', locals())  # 字典参数
			if user.password == password:
				# 往session字典内写入用户状态和数据
				request.session['is_login'] = True
				request.session['user_id'] = user.id
				request.session['user_name'] = user.name
				return redirect('/index/')
			else:
				# message = '密码不正确'
				return render(request, 'login/login.html', locals())
		else:
			return render(request, 'login/login.html', locals())
	login_form = forms.UserForm()
	return render(request, 'login/login.html')


def register(request):
	if request.session.get('is_login', None):
		return redirect('/index/')

	if request.method == 'POST':
		register_form = forms.RegisterForm(request.POST)
		message = '请检查填写的内容'
		if register_form.is_valid():
			username = register_form.cleaned_data.get('username')
			password1 = register_form.cleaned_data.get('password1')
			password2 = register_form.cleaned_data.get('password2')
			email = register_form.cleaned_data.get('email')
			sex = register_form.cleaned_data.get('sex')

			if password1 != password2:
				message = '两次输入的密码不一致'
				return render(request, 'login/register.html', locals())
			else:
				same_name_user = models.User.objects.filter(name=username)
				if same_name_user:
					message = '当前用户已存在'
					return render(request, 'login/register.html', locals())
				same_email_user = models.User.objects.filter(email=email)
				if same_email_user:
					message = '当前邮箱已被注册'
					return render(request, 'login/register.html', locals())
				new_user = models.User()
				new_user.name = username
				new_user.password = password1
				new_user.email = email
				new_user.sex = sex
				new_user.save()
				return redirect('/login/')
		else:
			return render(request, 'login/register.html', locals())
	register_from = forms.RegisterForm()
	return render(request, 'login/register.html', locals())


def logout(request):
	if not request.session.get('is_login', None):
		return redirect('/login/')
	request.session.flush()
	return redirect("/login/")
