from django import forms
from crudapp.models import Employee

class EmpReg(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ["empid","ename","ememail"]
		widgets = {
		"empid":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Employee Id"
			}),
		"ename":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Employee Name"
			}),
		"ememail":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Employee Email"
			}),
		}