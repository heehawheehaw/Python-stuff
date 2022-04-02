##aggregate elements from 2 or more iterable , creates a zip object with paired elements sotreed in tupels for each object

from re import L


username = ["Dude","Bro","Mister"]
password = ["p@ssword","abc123","guest"]
users = list(zip(username, password))
for i in users:
    print(i)
for key,value in users.items():
    print(key+":"+value)
    