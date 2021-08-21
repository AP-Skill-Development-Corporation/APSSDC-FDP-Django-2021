from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def static(request):
	return HttpResponse("<h1><center>This is a static page</center></h1")


def dynamicstr(request,name):
	return HttpResponse("<h1><center>My name is:"+name+"</center></h1>")


def dynamicint(request,rollno):
	return HttpResponse("<h1><center>My rollno is: {}</center></h1>".format(rollno))

def student(request,name,roll):
	return HttpResponse("<h1>Your Name is: <span style='color:green'>{}</span></br>Your Roll Number is: <span style='color:red'>{}</span></h1>".format(name,roll))

def empdetails(sr,empname):
	return HttpResponse("<h1>Hi Welcome User {}</h1><script>alert('Hi Welcome {}')</script>".format(empname,empname))

def tech(req):
	return render(req,"htmlfiles/sample.html")

def externalhtml(ret):
	return render(ret,"htmlfiles/exthtm.html")