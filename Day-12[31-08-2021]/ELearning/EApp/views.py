from django.shortcuts import render,redirect
from EApp.forms import CourseForm,SubCourseForm
from EApp.models import Courses

# Create your views here.

def home(req):
	return render(req,'html/home.html')

def about(req):
	return render(req,'html/about.html')

def contact(req):
	return render(req,'html/contact.html')

def courses(request):
	k = Courses.objects.all()
	if request.method == "POST":
		t = CourseForm(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/allcourses')
	t = CourseForm()
	return render(request,'html/allcourses.html',{'y':t,'g':k})

def courseupdate(request,y):
	z = Courses.objects.get(id=y)
	if request.method == "POST":
		v = CourseForm(request.POST,instance=z)
		if v.is_valid():
			v.save()
			return redirect('/allcourses')
	v = CourseForm(instance=z)
	return render(request,'html/crup.html',{'d':v})

def coursedelete(request,p):
	d = Courses.objects.get(id=p)
	if request.method == "POST":
		d.delete()
		return redirect('/allcourses')
	return render(request,'html/crdl.html',{'r':d})

def suballcourse(request):
	if request.method == "POST":
		k = SubCourseForm(request.POST)
		if k.is_valid():
			k.save()
			return redirect('/suball')
	k = SubCourseForm()
	return render(request,'html/suballcr.html',{'s':k})