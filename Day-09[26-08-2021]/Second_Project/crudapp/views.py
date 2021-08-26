from django.shortcuts import render,redirect
from crudapp.models import Employee
# Create your views here.

def showall(request):
	p = Employee.objects.all()
	if request.method == "POST":
		emid = request.POST['ed']
		empname = request.POST['en']
		empemail = request.POST['em']
		y = Employee(empid = emid,ename = empname, ememail = empemail)
		y.save()
		return redirect('/')
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
		return redirect('/')
	return render(request,'crud/updateemp.html',{'b':e})