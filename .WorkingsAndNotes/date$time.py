from datetime import data 
from datetime import time
from datetime import datetime
#make sure python file is diff from module you want to import
# python will look into dir , if no find will make a pyc file & compile it
today = date.today()
print(today)
print(today.day,today,month,today.year)
print("The weekday number is", today.weekday())
#WEEKDAY property can be used to aggregate into a list
days = ["mon","tue","wed","Thu","Fri","Sat","sun"]
print (days[today.weekday()])

today = datetime.now()
t= datetime.tim(datetime.now())

print(today.strftime("the current year is : %Y"))
print(today.strftime("%a, %d %B, %y"))
print(today.strftime("%I:%M:%S" %p))

print(str(today + timedelta(365)))
print(timedelta(days=365, hours=7, minutes=5))

print(str(today + timedelta(days=4, weeks=5)))
x =datetime.now() - timedelta(weeks=2,)
y = x.strftime("%A %B %d, %Y")
print(y)
daysAhead = date.today()
xmas = date(daysAhead.year, 12,25)
timetoxmas = xmas - daysAhead

import callendar
cal = calendar.TextCalendar(calendar.SUNDAY)
str = cal.formatmonth(2019, 4)
print(str)
for days in cal.itermonthdays(2019,4):
	print(days)
for name in calendar.month_name:
	print(name)
for day in calendar.day_name:
	print(day)
for m in range(1,13):
	cal = calendar.monthcalendar(2019,m)
	wk1 = cal[0]
	wk2=cal[1]
	if wk1[calendar.FRIDAY] != 0:
		meeting = wk1[calendar.FRIDAY]
	else:
		meeting = wk2[calendar.FRIDAY]
	print("%10s %d" % (calendar.month_name[m], meeting))



#computer epoch
import time 
print(time.ctime(0))
print(time.time())
time_object = time.localtime()
time_object = time.gmtime() # utc time
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

time_string = "20April, 2020"
time_object = time.strptime(time_string,"%d %B, %Y")
print(time_object)

#asc time
time_string = time.asctime(time_string)
time_tuple = (2020, 4, 20, 4,20,0, 0,0,0)

#mktime
time_string = time.mktime(time_string)
