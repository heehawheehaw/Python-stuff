x=20 
try:
	print(x)
except:
	pritn("variable is not defined.")
else:
	print("Hello")
finally:
	print("You may get & error if no variabl is specified")

b = 'Hello'
print(int(b))
while True:
	try:
		n = int(input("Enter a whole number: "))
		break
	except ValueError:
		print("No valid integer entered")
print("Great you have netered an integer")

try:
	n = 12/ int(input("Enter a whole number:"))
	print("The value of your number is ", n )
except ZeroDivisionError as e:
	print(e)
except ValueError as e:
	print(e)
finally:print("Hope you entered a valid whole number.")


'''
exceptions are erros that occurs during the execution of a program

*exception ; type of exception & exception error& builtin handler that respons to that type of erro
errors can be handled or caught by embedding your code in [try & except] statement blocks
there has to be at least one except clause with every try clause ; can catch different type of statements
defualt python handler is called if none is specified 
a [try] block lets you test for error
a [except] block lets you specify how to handle errors
a [finally] block lets you specify what code to execute regardless of what happens in try & except block 
a [else] block lets specity what coee to execute if no exception errors occurs 

'''