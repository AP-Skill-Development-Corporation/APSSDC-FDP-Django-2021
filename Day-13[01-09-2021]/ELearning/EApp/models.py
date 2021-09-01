from django.db import models

# Create your models here.

class Courses(models.Model):
	coname = models.CharField(max_length=120)

	def __str__(self):
		return self.coname

class SubCourses(models.Model):
	sbconame = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=8,decimal_places=2)
	desc = models.CharField(max_length=250)
	crid = models.ForeignKey(Courses,on_delete=models.CASCADE)

	