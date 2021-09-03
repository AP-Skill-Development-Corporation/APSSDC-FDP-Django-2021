from django import forms
from EApp.models import Courses,SubCourses,User
from django.contrib.auth.forms import UserCreationForm

class CourseForm(forms.ModelForm):
	class Meta:
		model = Courses
		fields = "__all__"
		widgets = {
		"coname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Newe Course Name",
			}),
		"cimage":forms.FileInput(attrs={
			"class":"form-control my-2",
			"placehodler":"Select an Image",
			})
		}

class SubCourseForm(forms.ModelForm):
	class Meta:
		model = SubCourses
		fields = ["crid","sbconame","price","desc"]
		widgets = {
		"crid":forms.Select(attrs={
			"class":"form-control",
			}),
		"sbconame":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter SubCourse Name",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Price",
			}),
		"desc":forms.Textarea(attrs={
			"class":"form-control my-2",
			"rows":5,
			"placeholder":"Enter Description"
			}),
		}

class RegForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username",
			}),
		}

class UsPfle(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","mobile","pcimg"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":True,
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Email",
			}),
		"mobile":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Mobile Number",
			}),
		}



