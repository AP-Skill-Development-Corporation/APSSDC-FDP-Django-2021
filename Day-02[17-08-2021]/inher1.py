class A:
    a,b=10,20
    def printMsg():
        print("hi i am super class")
        print("i unable to access sub class properties")
        

class B(A):
    c,d=30,34
    def printCnt():
        print("hi iam from sub class")
        print("i can able to access super class properties..")

obj = B
print(obj.a,obj.b)
obj.printMsg()
print(obj.c)
