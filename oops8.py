#class is a blue print for creating objects
class Accounts:
    bnkname="Abdul Akram Bank Pvt LTd"
    def __init__(self,bal,accno):
        self.bal=bal
        self.accno=accno
    def debit(self,amnt):
        self.bal-=amnt
        return f"The amount {amnt} has been debited",self.bal
    def credit(self,amnt):
        self.bal+=amnt
        return f"The amount {amnt} has been credited",self.bal
    def getbal(self):
        return f"The Balance in {self.accno} :",self.bal

ac1=Accounts(50000,786786)
print(Accounts.bnkname)
print(ac1.getbal())
print(ac1.debit(2000))
print(ac1.credit(5000))
#del ac1 is for deleting the obj and obj attribute
#__ac1 is for private attribute and private obj it can access only in the class level
print(ac1.credit(5000))


class Student:
    clgname="LORDS Institute of engg"
    def __init__(self,name):
        self.name=name
    def hello(self):
        print("Assalam Ualykum")
        

s1=Student("Abdul")
s2=Student("Pathan")
print(s1.name,'Its a object attribute different for all objects')
print(s2.clgname,'Its a class Attribute same for all objects')
print(s1.clgname)
print(s1.clgname)

list={'Abdul':'56','Akram':'57','Kareem':'99'}
print(type(list))

class Mercedez:
    name="Black"
    def __init__(self,name,model,cost):
        self.name=name
        self.model=model
        self.cost=cost
    def greet(self):
        return(f"Mubarak Brother for your {c1.name}")
c1=Mercedez("Brabus","2024",6700000)
print(c1.name,c1.model,c1.cost,c1.greet())
print("Practice Of Class and Object in OOPS")
class Students:
    def __init__(self,name,mths,eng,social):
        self.name=name
        self.mths=mths
        self.eng=eng
        self.social=social
    def average(self):
        sum=self.mths+self.eng+self.social
        average=sum//3
        return average
    
stud1=Students("Zyn",78,86,78)
print(stud1.average())
print("Inheritance is a imp concept in oops which is used to inherit the attributes and methods")
class Car:
    @staticmethod
    def start():
        return "The Car has been Started"
    @staticmethod
    def stop():
        return "The car has been stopped"

class Maruthi(Car):
    def __init__(self,name):
        self.name=name
class Ertiga(Maruthi):
    def __init__(self,types):
        self.types=types
        print(self.types)
car1=Maruthi("Swift")
car2=Maruthi("Wagonr")
car3=Ertiga("Diesel")
print(car3.start())
print(car3.stop())
#print(car2.name)
#print(car1.name)
#print(car1.start(),car1.name)
print(car2.stop(),car2.name)

print("Multiple Inheritance")

class A:
    namea="AbdulAkram"
class B:
    nameb="Moiz"
class c(A,B):
    namec="Maaz"
cse=c()
print(cse.namea)



    
        
    






















