from django.db import models

# Create your models here.

class Employee(models.Model):
	ename = models.CharField(max_length=120)
	empid = models.CharField(max_length=10)
	ememail = models.EmailField(max_length=120)
	