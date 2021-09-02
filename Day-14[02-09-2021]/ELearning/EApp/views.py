from django.shortcuts import render,redirect
from EApp.forms import CourseForm,SubCourseForm,RegForm
from EApp.models import Courses,SubCourses
from django.contrib import messages

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
		t = CourseForm(request.POST,request.FILES)
		if t.is_valid():
			t.save()
			messages.success(request,"Successfully Added Course to Courselist")
			return redirect('/allcourses')
	t = CourseForm()
	return render(request,'html/allcourses.html',{'y':t,'g':k})

def courseview(request,u):
	n = Courses.objects.get(id=u)
	return render(request,'html/courseview.html',{'f':n})

def courseupdate(request,y):
	z = Courses.objects.get(id=y)
	if request.method == "POST":
		v = CourseForm(request.POST,request.FILES,instance=z)
		if v.is_valid():
			messages.warning(request,"{} Subcourse Updated".format(z.coname))
			v.save()
			return redirect('/allcourses')
	v = CourseForm(instance=z)
	return render(request,'html/crup.html',{'d':v})

def coursedelete(request,p):
	d = Courses.objects.get(id=p)
	if request.method == "POST":
		messages.info(request,"{} Course Deleted Successfully".format(d.coname))
		d.delete()
		return redirect('/allcourses')
	return render(request,'html/crdl.html',{'r':d})

def suballcourse(request):
	dr,h = {},0
	c = SubCourses.objects.all()
	t = Courses.objects.all()
	for j in c:
		for i in t:
			if j.crid_id == i.id:
				dr[h] = i.coname,j.sbconame,j.price,j.desc,j.id
				h+=1
	# print(dr.values())
	if request.method == "POST":
		k = SubCourseForm(request.POST)
		if k.is_valid():
			k.save()
			return redirect('/suball')
	k = SubCourseForm()
	return render(request,'html/suballcr.html',{'s':k,'z':dr.values()})

def subcourseup(request,v):
	y = SubCourses.objects.get(id=v)
	if request.method == "POST":
		e = SubCourseForm(request.POST,instance=y)
		if e.is_valid():
			e.save()
			return redirect('/suball')
	e = SubCourseForm(instance=y)
	return render(request,'html/subupdt.html',{'x':e})

def subcoursedel(request,h):
	d = SubCourses.objects.get(id=h)
	if request.method == "POST":
		d.delete()
		return redirect('/suball')
	return render(request,'html/subdel.html',{'t':d})

def registration(request):
	if request.method == "POST":
		k = RegForm(request.POST)
		if k.is_valid():
			k.save()
			return redirect('/')
	k = RegForm()
	return render(request,'html/register.html',{'d':k})










