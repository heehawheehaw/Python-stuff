#default parameter value
def student_names(names="Bluelime"):
	print("Hellow" + names)
student_names()
student_names("John")
student_names("Jane")

def appendItem(itemName, itemList = []):
	itemList.append(itemName)
	return itemList
print(appendItem('notebook'))
print(appendItem('pencil'))
print(appendItem('eraser'))

def addItemToDictionary(itemName, quantity, itemList = {}):
	itemList[itemName] = quantity
	return itemList
print(addItemToDictionary('notebook', 4))
print(addItemToDictionary('pencil', 1))
print(addItemToDictionary('eraser', 1))
#usenone is good practice
print('#list')
def appendItem(itemName, itemList=None):
	if itemList == None:
		itemList = []
	itemList.append(itemName)
	return itemList
print(appendItem('notebook'))
print(appendItem('pencil'))
print(appendItem('eraser'))
print('\n\n#dictionary')
def addItemToDictionary(itemName, quantity, itemList = None):
	if itemList == None:
		itemList = {}
	itemList[itemName] = quantity
	return itemList
print(addItemToDictionary('notebook', 4))
print(addItemToDictionary('pencil', 1))
print(addItemToDictionary('eraser', 1))

#keyword arguments or kwargs
def more_num(a, b=7,c=10):
	print("a is ",a, "and b is ",b,"while c is ",c)

more_num(3,7)
more_num(23,c=17)
more_num(c=40,a=80)

def greeting():
	def say_hello():
		return "Hellow"
	return say_hello()
hello = greeting()


#passign functions as arguments to other functions 
def mynum(b):
	return b+1
def addnum(c):
	newnum= 17
	return c(newnum)
print(addnum(mynum))

#variable argument or VarArgs
def total_numbers(a=7 , *numbers, **phonebook):
	print("My fav number is ", a)
	for num in numbers:
		print("num", num)
	for name,phone_number in phonebook.items():
		print(name,phone_number)
total_numbers(7,1,2,3,Jane=2222,John=4444,Angela=5555)

def foo(x, *args, **kwargs):
	kwargs['name'] = 'Alice'
	new_args = args + ('extra',)
	bar(x, *new_args, **kwargs)

#lambda
a = lambda b: b+4
print(a(4))
c= lambda d,e : d + e
print(c(7,8))
def ghost_number(n):
	return lambda f : f * n
double_num = ghost_number(2)
print(double_num(20))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
fullname("Leonhard","Euler")

def build_quadratic_functions(a,b,c):
	"""returns the function f(x) = ax^2 +bx+c"""
	return lambda x: a*x**2 + b*x + c
f = build_quadratic_functions(2,3,-5)(13)

#decorators
def my_decorator(function):
	def wrapper():
		myfunc = function()
		convert_uppercase = myfunc.upper()
		return convert_uppercase
	return wrapper
@my_decorator
def say_hello():
	return "hello world"
#decorate = my_decorator(say_hello)
print(decorate())

def f1():
	print("Called f1")
def f2(f):
	f()
f2(f1)
#wrapperfunction
def f1(func):
	def wrapper(*args, **kwargs):
		print("Started")
		val = func(*args, **kwargs)
		print("Ended")
		return val
	return wrapper
@f1
def f(a, b=9):
	print(a,b)
@f1 
def add(x,y):
	return x+y
print(add(4,5))


#docstrings, help, pydoc?
def add_numbers(d,e):
	''' Adding 2 numbers.
	The Values must be integers'''
	print(d + e)
#	:param d:
#	:param e:
#	:return:
#	'''
add_numbers(8,4)
pritn(add_numbers._doc_)