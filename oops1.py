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
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.status='available'

    def borrow(self):
        if self.status == 'available':
            self.status = 'borrowed'
            return True
        return False

    def return_book(self):
        if self.status == 'borrowed':
            self.status = 'available'
            return True
        return False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_available_books(self):
        available_books = [book for book in self.books if book.status == 'available']
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.borrow():
                print(f"You borrowed '{title}'")
                return
        print(f"'{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.return_book():
                print(f"You returned '{title}'")
                return
        print(f"'{title}' was not borrowed.")

# Example usage:
'''library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)
library.add_book(book2)
library.display_available_books()
library.borrow_book("The Great Gatsby")
library.display_available_books()
library.return_book("The Great Gatsby")
library.display_available_books()'''
Lib=Library()
book1=Book("The Rich Dad","Robert")
Lib.add_book(book1)
Lib.display_available_books()
Lib.borrow_book("The Rich Dad")
Lib.return_book("The Rich Dad")
Lib.display_available_books()

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














        
        
    
