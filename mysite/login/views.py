from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms

# Create your views here.


def index(request):
	pass
	return render(request, 'login/index.html')


def login(request):
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
				# print(username, password)
				return redirect('/index/')
			else:
				# message = '密码不正确'
				return render(request, 'login/login.html', locals())
		else:
			return render(request, 'login/login.html', locals())
	login_form = forms.UserForm()
	return render(request, 'login/login.html')


def register(request):
	pass
	return render(request, 'login/register.html')


def logout(request):
	pass
	return redirect("/login/")
