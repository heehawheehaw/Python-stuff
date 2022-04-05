#functions that can manipulate strings
'''
len() # returns character length of a string
index()#:returns position of a string or character
capitalize()#convert first character of string to upper 
upper()#convert string to uppercase
islower()/isupper()# check if all characters are lower/upper
[find()]:find first index occurence of string or character
[count()]:counts occurence of string or character
[split()]:split string into python lists
[\n]:separate string or character to another line
[+]:concatenation,addsstring together
[replace()]: replace string or charactera
join()
strip()
'''

'''
escape sequences
\\ : backslash
\' : single quote
\" : double quote
\a : ASCII bell
\b : ASCII backspace
\f : ASCII formfeed
\n : ASCII linefeed
\r : ASCII carriage return
\t : ASCII horizontal tab
\v : ASCII vertical tab
\ooo : Char with Odal Value OO
\schh : Char with Value hh
'''


'''
F- string, string literal prefixed with f
-contains expressions inside curly braces which are replaced with values
-expression is evaluated at runtime & then formatted
-not a constant value
'''
name ="Bime"
age= "35"
profession = "hacker"
print(f"Hello,{name}. You are {age} years old.")
message = (
    f"Hi {name}"
    f"You are a {profession}"
    f"You have been teaching online for {age} years"
)
print(message)


'''
format using % operator 
-%s inject strings
-%d inject integers 
-%f floating point values ; use format %a.bf i.e. a=minimum number of digits present in string, bf= digits to be displayed after decimal point
-%b binary format
'''
print("fasdfasdfasdfasdfsdf" %'asdfasdfasdf')
x='asdfasdf'
print('asdfasdf %s asdf %s asdfsdf'%('asdfasdf',x))


'''
format using format()method 
float precision with the format()method 
synta -> {[index]:[width][.precision][type]}
d - for integers 
f - floating point numbers 
b - binary numbers 
o - octal numbers 
x - ocatl hexadecimal numbers 
s - string 
e - floating point in a n exponent format 
'''
print('we all are {}.'.format('equal'))
print('{2} {1} {0}'.format('asdfsdf','asdfasdf','asdfasd')
)


'''
format with string template class 
'''
from string import template 
n1 = 'Hello '
n2 = 'Geasdgasdf'
n=Template ('$n3! This is $n4')
print(n.substitue(n3=n1,n4=n2))