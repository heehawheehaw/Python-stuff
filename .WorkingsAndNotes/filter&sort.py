#filter creates a collection from an iterables

friends =[("Racheal",19),
("monica",18),
("phoebe",17)]
age = lambda data:data[1] >= 18
drinking_buddies = list(filter(age, friends))


#reduce fucntion, applies iterable to single iterable value with a funciton
letters = ["h","e","l","l","o"]
import functool
word = functool.reduce(lambda x,y,:x+y,letters)
print(word)
factorial = [5,4,3,2,1]
result = functool.reduce(lambda x,y,:x*y,factorial)
print(result)