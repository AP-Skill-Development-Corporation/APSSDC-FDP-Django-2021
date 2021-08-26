from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def samplebs(request):
	return render(request,'ht/samplebs.html')

def btregi(request):
	return render(request,'ht/btregst.html')