from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	mobile = models.CharField(max_length=10)
	pcimg = models.ImageField(upload_to="Profiles/",default="profile.jpeg")


class Courses(models.Model):
	coname = models.CharField(max_length=120)
	cimage = models.ImageField(upload_to="Courses/",default="courses.jpeg")
	usid = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.coname

class SubCourses(models.Model):
	sbconame = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=8,decimal_places=2)
	desc = models.CharField(max_length=250)
	crid = models.ForeignKey(Courses,on_delete=models.CASCADE)



	