#import os

#print(os.getcwd())

#os.chdir("./documentsd")
#print(os.getcwd())

#os.mkdir("createNews")
#os.chdir("./createNews")


#dir = os.getcwd()
#print("direc",dir)
#path = os.path.join(dir,"createNew")
#print(path)
#os.rmdir(path)

#import sys

#name = sys.stdin.readline().strip()
#sys.stdout.write("syee", + name)


#task
import datetime
import calendar

#date = "2021-04-3 04:45"
#print(datetime.datetime(2023,7,1,10,30))

#print(datetime.datetime.now().timestamp())
#print(datetime.datetime.now().weekday())
#print(calendar.month(2020))
#print(calendar.calendar(2022))
#print(calendar.isleap(2022))
print(calendar.weekday(2022,7,7))