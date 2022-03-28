import time as t
t.localtime()
time_now = t.localtime()
print("Transaction completed at", str(time_now,tm_hour) + "h" + str(time_now,tm_min) + "m"
t.time()
time_now = t.time()
delivery_time = time_now + (86400*7)
t.localtime(delivery_time)
t.sleep(5)

import matplotlib.pyplot as plt
x = [1,7,3,4]
y = [1500, 1200,1100,1800]
plt.plot(x,y)
plt.show()
legend = ["january", "February", "March", "April"]
plt.xticks(x,legend)
plt.plot(x,y)
plt.show()
plt.bar(x,y)
plt.ylabel("Sales in US$")
plt.title("Monthly")
plt.show()

#TypingSpeed project
import matplotlib.pyplot as plt 
import time as t 
times = []
mistakes = 0 
print("This prohram will ehlp you type faster. You will have to type the word 'programming as fast as you can for five times")
input("Press enter to continue")

while len(times)<5:
	start = t.time()
	word = input("Type the word: ")
	end = t.time()
	time_elapsed - end - start
	times.append(time_elapsed)
	if(word.lower() != "programming"):
		mistakes +=1
print("You made"+ str(mistakes) + "mistakes.")
print("Now lets see your evolution")
t.sleep(3)
x = [1,2,3,4,5]
y = times 
plt.plot(x,y)
legend = ["1","2","3","4","5"]
plt.xticks(x,legend)
plt.ylabel('Time in secs')
plt.title('Your typing evolution')
plot.show()