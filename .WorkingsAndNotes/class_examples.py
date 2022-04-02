class Instructors:
	companyName = "Bluelime"

	def __init__(self,course):
		self.course = course

	def printinfo(self):
		print("My Company name is ", Instructors.companyName)

elearning = Instructors("Python for beginners")

bls = Instructors("Django for beginners")

bls.course = "HTML"
bls.printinfo()
print(bls.course)


#class , 
class User:
	pass
user1 = user() # an object
user1.first_name = "dave" # a variable name
user1.last_name = "Bowman"
#fields , data attached to an object
print(user1.first_name)
print(user1.last_name)
first_name="arthur"
last_name="asdf"
user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"
user.age= 37
user2.favourite_book = "2002 ; a space odyssey"

class User:
	"""A mmebr of ff , for now we are only sotring their name & 
	    only sotring their name & birthday."""
	def __init__(self, full_name, birthday):
		self.name = full_name
		self.birthday = birthday # yyyymmdd
		name_pieces = full_names.split(" ")
		self.first_name = name_pieces[0]
		self.last_name = name_pieces[-1]
	def age(self):
		today = datetime.date(1001,5,14)
		yyyy = int(self.birthday[0:4])
		mm = int(self.birthday[4:6])
		dd = int(self.birthday[6:8])
		dob = datetime.date(yyyy,mm,dd)
user = User("Dave Bowman" , "123123")
help(User)\


#abstraction
class Shape:
	def area(self):
		pass
	def perimeter(self):
class Square(Shape):
	def __init__(self,side):
		self.side = side 
	myshape = Shape()
from abc import ABC, abstractmethod 
class Shape(ABC):
	@abstractmethod
	def area(self):
		pass
	@abstractmethod
	def perimeter(self):
		pass
class Square(Shape):
	def __init__(self,side):
		self.side = side 
	def area(self):
		return self.__side* self.__side
	def perimeter(self):
		return 4*self.__side
mysquare = Square(5)
print(mysquare.area())
print(mysquare.perimeter())

#encapsulation
class Cars:
	def __init__(self,speed,colour):
		self.speed=speed
		self.color=colour
	def set_speed(self,value):
		self.speed = value
	def get_speed(self):
		return self.get_speed
ford = cars(250,"green")
nissan = Car(300,"red")
toyota = Cars(350,"blue")
ford,set_speed(750)
ford.__speed = 800

#inheritance
class Person:
	def __init__(self,fname,lname):
		self.firstname = full_name
		self.lastname = last_name
	def printname(self):
		print(self.firstname,self.lastname)
florist = Person("Jane", "Flowers")
florist.printname()
class Lawyers(Person):
	pass
happy_lawyers = Lawyers("Jack","Smiley")
happy_lawyers.printname()
class Lawyers(Person):
	def __init__(self,fname,lname):
		Person.__init__(self,fname,lname)
	def printinfo(self):
		print(self,firstname,self.lastname)

#polymorphism
def addNumbers(a,b,c=1):
	return a + b + c
print(addNumbers(8,9))
print(addNumbers(8,9,4))
class Uk():
	def capital_city(self):
		print("London is the capital of UK")
	def language(self):
		print("English is the primary language")
queen = UK()
queen.capital_city()
zara = spain()
zara.capital_city()
for country in (queen,zara):
	country.capital_city()
	country.language()
def europe(eu):
	eu.capital_city()

#coreyschafer
#class is blueprint for each instances
#instance variables contains data for each instance
#class variable
#regular methods ; takes instance as first arg
#class methods ; takes class as first arg
#static methods ; dont pass anything
#special methods; 
#property decorators
class Employee:
	num_of_emps = 0
	raise_amount = 1.04
	def __init__(self, first, last, pay):
		self.first = first 
		self.last = last 
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
	   #when create first method of class, receive first instance as argument auto
	    Employee.num_of_emps += 1 
	def fullname(self):
		return '{} {}'.format(self.first , self.last)
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or if day.weekday() == 6:
			return False
		return True
	def __repr__(self):
		return "Employee('{}','{}',{})".format(self.first, self.last,self.pay)
	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)
	def __add__(self, other):
		return self.pay + other.pay
	@property
	@fullname.setter
	@fullname.deleter
	@fullname.getter
 
 emp1 = Employee('Corey','Schafer' , 5000)
 emp1.set_raise_amount = 1.05
 Employee.set_raise_amt(1.05)
 empstr1 = 'John-Doe-700000'
 newemp1=Employee.from_string(empstr1)
 repr(emp1)
 str(emp1)

 class Developer(Employee):
 	raise_amt = 1.10
 	def __init__(self, first, last, pay, prog_lang):
 		super().__init__(first, last, pay)
 		self.prog_lang = prog_lang
 		Employee.__init__(self, first, last, pay)
dev1 = Developer('Test', 'Employee' , 60000, 'python')
 print(help(Developer))
 dev1.apply_raise()

 class Manager(Employee):
 	def __init__(self, first, last, pay, employees=None):
 		super(). __init__(first, last, pay)
 		if employees is None:
 			self.employees = []
 		else:
 			self.employees = employees
 	def add_emp(self, emp):
 		if emp not in self.employees:
 			self.employees.append(emp)
 	def remove_emp(self, emp):
 		if emp in self.employees:
 			self.employees.remove(emp)
 	def print_emps(self):
 		for emp in self.employees:
 			print('-->', emp.fullname())
mgr1 = Manager('Sue' , 'Smith', 90000, [dev1])
mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)

isinstance()#tell if instance is object of class
issubclass()#tell if subclass of another 


#method overriding, allow subclass to provide specific implementation provided by parent class
class Animal:
	def eat(self):
		print("This animal is eating")

class Rabbit(Animal):
	def eat(self):
		print("This rabbit is eating a carrot")
rabbit = Rabbit()


#method chaining, calling multiple methods sequentially, each call performs an action on the same object
class Car:
	def turn_on(self):
		print("You start the engine")
		return self
    def drive(self):
		print("You drive the car")
		return self
	def brake(self):
		pritn("You step on the brakes")
		return self
	def turn_off(self):
		print("You turn off the engine")
		return self
car = Car()
car.turn_on()\
	.drive()\
		.brake()\
			.turn_off()



#super function , gives access to methods of parent class, return a temporary object
class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width
class Square(Rectangle):
	def __init__(self, length, width):
		super().__init__(length,width)
	def area(self):
		return self.length*self.width
class Cube(Rectangle):
	def __init__(self,length,width,height):
		super().__init__(length,width)
		self.height = height
	def volume(self):
		return self.length*self.width*self.height
square = Square(3,3)
cube = Cube(3,3,3)



#ducktyping, class of object is less important then the method
class Duck:
	def walk(self):
		print("This duck is walking")
	def talk(self):
		print("This duck is quacking")
class Chicken:
	def walk(self):
		print("This chicken is waling")
	def talk(self):
		print("This chicken is clucking")
class Person:
	def catch(self,duck):
		duck.walk()
		duck.talk()
		print("You caught the critter!")
duck = Duck()
chicken = Chicken()
person = Person()
person.catch(chicken)



