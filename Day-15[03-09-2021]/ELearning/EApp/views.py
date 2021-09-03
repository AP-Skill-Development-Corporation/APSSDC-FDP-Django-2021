from django.shortcuts import render,redirect
from EApp.forms import CourseForm,SubCourseForm,RegForm,UsPfle
from EApp.models import Courses,SubCourses,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(req):
	return render(req,'html/home.html')

def about(req):
	return render(req,'html/about.html')

def contact(req):
	return render(req,'html/contact.html')

@login_required
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

@login_required
def courseview(request,u):
	n = Courses.objects.get(id=u)
	return render(request,'html/courseview.html',{'f':n})

@login_required
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

@login_required
def coursedelete(request,p):
	d = Courses.objects.get(id=p)
	if request.method == "POST":
		messages.info(request,"{} Course Deleted Successfully".format(d.coname))
		d.delete()
		return redirect('/allcourses')
	return render(request,'html/crdl.html',{'r':d})

@login_required
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

@login_required
def subcourseup(request,v):
	y = SubCourses.objects.get(id=v)
	if request.method == "POST":
		e = SubCourseForm(request.POST,instance=y)
		if e.is_valid():
			e.save()
			return redirect('/suball')
	e = SubCourseForm(instance=y)
	return render(request,'html/subupdt.html',{'x':e})

@login_required
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
			return redirect('/login')
	k = RegForm()
	return render(request,'html/register.html',{'d':k})

@login_required
def dashboard(request):
	return render(request,'html/dashboard.html')

@login_required
def profile(request):
	return render(request,'html/profile.html')

@login_required
def updateprofile(request):
	k = User.objects.get(id=request.user.id)
	if request.method == "POST":
		j = UsPfle(request.POST,request.FILES,instance=k)
		if j.is_valid():
			j.save()
			return redirect('/pfle')
	j = UsPfle(instance=k)
	return render(request,'html/updfle.html',{'t':j})







