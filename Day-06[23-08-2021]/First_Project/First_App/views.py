from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def static(request):
	return HttpResponse("<h1><center>This is a static page</center></h1")


def dynamicstr(request,name):
	return HttpResponse("<h1><center>My name is:"+name+"</center></h1>")


def dynamicint(request,rollno):
	return HttpResponse("<h1><center>My rollno is: {}</center></h1>".format(rollno))


def tech(req):
	return render(req,"htmlfiles/sample.html")

def externalhtml(ret):
	return render(ret,"htmlfiles/exthtm.html")

def myform(request):
	if request.method == 'POST':
		# print(request.POST)
		uname = request.POST['uname']
		rollno = request.POST['rollno']
		email = request.POST['email']
		#print(uname,rollno,email)
		data = {'username':uname,'rno':rollno,'emailId':email}
		return render(request,'htmlfiles/display.html',data)

	return render(request,'htmlfiles/myform.html')

