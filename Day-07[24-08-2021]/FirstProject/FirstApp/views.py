from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("Hi good morning to all")


def btregi(request):
	return render(request,'html/btregst.html')
