from django.shortcuts import render

# Create your views here.

def home(req):
	return render(req,'html/home.html')

def about(req):
	return render(req,'html/about.html')

def contact(req):
	return render(req,'html/contact.html')

def courses(request):
	return render(request,'html/allcourses.html')


