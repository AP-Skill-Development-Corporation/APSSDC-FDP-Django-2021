from django.shortcuts import render,redirect
from crudapp.models import Employee
from crudapp.forms import EmpReg

# Create your views here.

def showall(request):
	p = Employee.objects.all()
	if request.method == "POST":
		emid = request.POST['ed']
		empname = request.POST['en']
		empemail = request.POST['em']
		y = Employee(empid = emid,ename = empname, ememail = empemail)
		y.save()
		return redirect('/ty')
	return render(request,'crud/details.html',{'e':p})

def viewemployee(request,t):
	y = Employee.objects.get(id=t)
	return render(request,'crud/viewemp.html',{'et':y})

def updateemployee(request,k):
	e = Employee.objects.get(id=k)
	if request.method == "POST":
		e.empid = request.POST['emid']
		e.ename = request.POST['empna']
		e.ememail = request.POST['enm']
		e.save()
		return redirect('/ty')
	return render(request,'crud/updateemp.html',{'b':e})

def deleteemployee(request,m):
	n = Employee.objects.get(id=m)
	if request.method == "POST":
		n.delete()
		return redirect("/")
	return render(request,'crud/dltemp.html')

def detail(request):
	y = Employee.objects.all()
	if request.method == "POST":
		ec = EmpReg(request.POST)
		if ec.is_valid():
			ec.save()
			return redirect('/')
	ec = EmpReg()
	return render(request,'crud/dt.html',{'t':ec,'u':y})

def updemp(request,r):
	n = Employee.objects.get(id=r)
	if request.method == "POST":
		h = EmpReg(request.POST,instance=n)
		if h.is_valid():
			h.save()
			return redirect('/')
	h = EmpReg(instance=n)
	return render(request,'crud/updemply.html',{'s':h})