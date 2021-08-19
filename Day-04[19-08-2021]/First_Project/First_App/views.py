from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def static(request):
	return HttpResponse("<h1><center>This is a static page</center></h1")


def dynamicstr(request,name):
	return HttpResponse("<h1><center>My name is:"+name+"</center></h1>")


def dynamicint(request,rollno):
	return HttpResponse("<h1><center>My rollno is: {}</center></h1>".format(rollno))