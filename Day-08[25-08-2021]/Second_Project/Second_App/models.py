from django.db import models

# Create your models here.


class Register(models.Model):
	name = models.CharField(max_length= 50)
	email = models.EmailField(max_length = 50)

class SignUp(models.Model):
	fname = models.CharField(max_length = 50)
	age = models.IntegerField()

	class Meta:
		db_table = 'login'




