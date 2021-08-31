from django import forms
from EApp.models import Courses,SubCourses

class CourseForm(forms.ModelForm):
	class Meta:
		model = Courses
		fields = "__all__"
		widgets = {
		"coname":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Newe Course Name",
			}),
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