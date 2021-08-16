Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Hi:
	a,b=10,20.4
	def display():
		print("hi all , welcome to django workshop")

		
>>> Hi.a
10
>>> type(Hi.a)
<class 'int'>
>>> type(Hi.b)
<class 'float'>
>>> Hi.display
<function Hi.display at 0x038ED738>
>>> Hi.display()
hi all , welcome to django workshop
>>> class Hello:
	name = "APSSDC"
	program_name = "Dango"
	def display():
		print("welcome to django")

		
>>> obj = Hello
>>> obj.name
'APSSDC'
>>> obj.program_name
'Dango'
>>> obj.display()
welcome to django
>>> obj1.Hello
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    obj1.Hello
NameError: name 'obj1' is not defined
>>> obj1 =Hello
>>> obj1.name
'APSSDC'
>>> obj3  = Hello()
>>> obj3.name
'APSSDC'
>>> obj3.display()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    obj3.display()
TypeError: display() takes 0 positional arguments but 1 was given
>>> class Cons:
	def __init__(self):
		print("hi all, i am constructor")
	def display():
		print("i am not constructor method")

		
>>> cns = Cons
>>> cns1 = Cons()
hi all, i am constructor
>>> cns1.display()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    cns1.display()
TypeError: display() takes 0 positional arguments but 1 was given
>>> class Cons:
	def __init__(myself):
		print("hi all, i am constructor")
	def display(myself):
		print("i am not constructor method")

		
>>> ct   = Cons()
hi all, i am constructor
>>> ct.display()
i am not constructor method
>>> class PCons:
	def __init__(self,firstname,lastname):
		self.fname = firstname
		self.lname = lastname
		print("i am belongs to parameterized cons")
	def show(self):
		print(self.fname,self.lname)

		
>>> obj = PCons("abdul","sk")
i am belongs to parameterized cons
>>> obj.show()
abdul sk
>>> class Register:
	def __init__(self,name,email):
		self.name = name
		self.email = email

		
>>> class Register:
	def __init__(self,name,email):
		self.name = name
		self.email = email
	def profile(self,phno,age):
		self.age = age
		self.phno = phno

		
>>> obj = Register("ravi","ravi@gmail.com")
>>> self.name
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    self.name
NameError: name 'self' is not defined
>>> obj.self.name
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    obj.self.name
AttributeError: 'Register' object has no attribute 'self'
>>> obj.name
'ravi'
>>> obj.email
'ravi@gmail.com'
>>> obj.profile(9807654321,27)
>>> obj.age
27
>>> obj.phno
9807654321
>>> 
