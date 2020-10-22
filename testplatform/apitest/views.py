from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.


def welcome(request):
	pass
	return render(request, 'welcome.html')


def default(request):
	return HttpResponse("火星人~~ 欢迎来到地球！！😋")


def home(request):
	return render(request, 'home.html')


def child(request, eid, oid):
	return render(request, eid)


def login(request):
	pass
	return render(request, 'login.html')


def register(request):
	pass
	return render(request, 'register')


def login_action(request):
	username = request.GET['username']
	password = request.GET['password']
	print(username, password)

	from django.contrib import auth
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		return HttpResponseRedirect('/home/')
	else:
		return HttpResponse('')
