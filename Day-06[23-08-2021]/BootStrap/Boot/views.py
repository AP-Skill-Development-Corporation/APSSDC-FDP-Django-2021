from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def samplebs(request):
	return render(request,'ht/samplebs.html')