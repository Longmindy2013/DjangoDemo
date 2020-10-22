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
