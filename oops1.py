def welcome():
    print('Akram')
try:
    a=int
    b=int
except ValueError:
    print("Invalid")

class Car:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
class Toyoto(Car):
    def __init__(self,name,year):
        self.year=year
        self.name=name
c1=Toyoto('Abdul',1999)
print(c1.name)

class Account:
    def __init__(self,accno,accpswd):
        self.accno=accno
        self.__accpswd=accpswd
    def getpswd(self):
        return self.__accpswd
#self.__accpswd is private attribute it cant be accessed outside the class but can be accessed in class
acc1=Account(786,"abdul123")
print(acc1.accno)
print(acc1.getpswd())

class Account:
    def __init__(self,actype):
        self.actype=actype
        print(self.actype)
    @staticmethod
    def start():
        print("Account created")
    @staticmethod
    def stop():
        print("Account Deactivated")
class person(Account):
    def __init__(self,acname,accbal,actype):
        super().__init__(actype)
        self.acname=acname
        self.actype=actype
        self.accbal=accbal
ac1=person("0706","5676","Savings")
print(ac1.actype)

class Person:
    #.__class__.name is for change the class attribute
    name="Anonymous"
    #def changename(self,name):
        #self.__class__.name=name
        #return Person.name
    @classmethod
    def changename(cls,name):
        cls.name=name
        return cls. name
        

p1=Person()
print(p1.changename("AbdulAkram"))
print(Person.name)
class Cse:
    def __init__(self,java,python,c):
        self.java=java
        self.python=python
        self.c=c
    @property
    def percentage(self):
        return str((self.java+self.c+self.python)/3) +"%"
abd1=Cse(56,78,98)
print(abd1.percentage)


class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownum(self):
        return f"{self.real}i+{self.img}j"
    
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return Complex(newreal,newimg)
    def __sub__(self,num2):
        newreal=self.real-num2.real
        newimg=self.img-num2.img
        return Complex(newreal,newimg)
    
num1=Complex(10,6)
num2=Complex(6,2)
print(num1.shownum())
print(num2.shownum())
num3=num1-num2
print(num3.shownum())














        
        
    
