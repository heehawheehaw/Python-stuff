#a flow of execution , like separate order of instructions
#each thread takes a turn running to achieve concurrency
#global interpreter lock(GIL) , allow only1 thread to hold the contorl of the python interpreter
#cpu bound (multiprocessing), program that spends most of its time waiting for internal events(e.g. cpu)
#io bound (multithreading), program spend most of its time for  external input(user input etc)

import threading
import time
from tkinter import Y

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")
def drink_coffe():
    time.sleep(4)
    print("You drink coffee")
def study():
    time.sleep(5)

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffe, args=())
y.start()

x.join()
y.join()
z.join()

#eat_breakfast()
#drink_coffe()
#study()

print(threading.active_count())
print(threading.enumerate())


#daemon threads, a thread that runs in the background , not important for programs to run
#program will nto wait for daemon threads to complete
#non daemone thread cannot normally be killed , staty alive until taks its comlte

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1 
        print("Logged in for:",counts,"seconds")
x = threading.Thread(target=timer)
x.start()
answer = input("Do you wish to exit")

x.setDaemon(True)
print(x.isdaemon)


#multiprocessing, run task in parallel on diff cpu cores 
from multiprocessing import Process, cpu_count
import time
def counter(num):
    count = 0
    while count < num:
        count += 1 
def main():
    print(cpu_count())
    a = Process(target=counter , args=(250000000))
    b = Process(target=counter , args=(250000000))
    c = Process(target=counter , args=(250000000))
    d = Process(target=counter , args=(250000000))
    a.start()
    b.start()
    c.start()
    d.start()
    a.join()
    b.join()
    c.start()
    d.start()
    print("finished in:", time.perf_counter(),"seconds")
if __name__ == '__main__':
    main()