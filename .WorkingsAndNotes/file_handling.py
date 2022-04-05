f = open("myfile.txt") #file object assigned to a variable
#if dont specify mode , will default to read
#if not in same directory need to specify path
# e.g. f = open('c:\\myfolders\myfile.txt)
print(f.readable())
print(f.read())
print(f.read(11))#counts untill 9 characters
print(f.readline())
print(f.readlines()) #turns into a list
for i in f:
	print(i)
f.close() #always close file
print(f.readable())

f = open("myfile.txt", 'w')
f.write("\nHappiness is from within")
f.close()

'''
python has ab built in file object which allows interactions with file in programs
open(),read(),readline(),readlines(),write().writelines(),append(),Close()
python file access mode
r,r+,w,w+,rb,a,t,x
'''
#accessing file object attributes
f= open("myfile.txt")
print(f.name)
print(f.mode)
print(f.closed)
f.close()

'''
file object have attributes
file poitners is the position that operations start from when file being interacted with in 
-by default , set to begining to file (rmode)
-[tell()] can show current file pointer position
-[seek()] ; set position of pointer
'''

#file pointers
f=open('myfile.txt')
print(f.read())
print(f.tell())
print(f.seek(0))
f.close()

import os 
os.rename('quotes.txt','quotes2.txt')
os.remove('quotes2.txt')
os.rmdir('folder')

#file detection
import os
path = "C:\\Users\Users\\Desktop\IloveBalles.txt"
if os.path.exists(path):
	print("That location exists!")
	if os.path.isfile(path):
		print("That is a file!")
	elif os.path.isdir(path):
		print("That is a directory!")
else:
	print("location exists")

#file reading/writing
text = "yoooo\nThis is some text\nhave a good one"
with open('test.txt','w') as file:
	file.write(text)

#copying files
import shutil
shutil.copyfile('test.txt','copy.txt') #src,dst
#copy() = copyfile()+permissionmode+destination_can_be_directory
#copy2() = copy()+copies_metadata i.e. file creationdate&time

#movefiles
import os
source = "test.txt"
destination = "C:\User\Cakow\Desktop"
try:
	if os.path.exists(destination):
		print("There is already a file!")
	else:
		os.replace(source,destination)
		print(source+"was")
except FileNotFoundError:
	print(source+"was not found")

#delete files
import os 
import shutil
path = "test.txt"
try:
	#os.rmdir(path)
	#os.remove(path)
	shutil.rmtree(path)
except FileNotFoundError:
	print("That file was not found")
except PermissionError:
	print("You do not have permission")
except OSError:
	print("You cannot delete that using the")
else:
	print(path+"was deleted")

