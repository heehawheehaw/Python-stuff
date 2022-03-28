# list comprehension, can condense for loops
# list = [expression for item in iterable if condition]
squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)

squares = [i*i for i in range(1,11)]
print(squares)

students = [100,90,80,70,60,40,30,20,10]
passed_students = [i for i in students if i >= 60]
passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)

#dictionary comprehension
# dictionary = {key:expression for (key,value) in iterable}
cities_in_f = {'new york':32,'boston':75},'los angeles':100 , 'chicago':50}
cities_in_c = {key:() for (key,((value-32)*(5/9))) in cities_in_f.items()}
print(cities_in_C)
sunny_weather = {key: value for (key,value) in weather.items if value =="sunny"}