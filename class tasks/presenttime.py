import random #a file
import time #a file

random.random() #gives values between 0 and 1. this function is in a random module
random.randint(10, 50) #generates range of values
time.time() #time() - a function inside the file

current_time = time.time()
total_seconds = int(current_time)

seconds = total_seconds % 60 #extract total seconds
total_minutes = total_seconds // 60 #convert total seconds to total minutes
minutes = total_minutes % 60 #extract total minutes
total_hours = total_minutes // 60 #convert total minutes to total hours
day = (total_hours % 24) + 1 #extract the total hours

current_second = seconds % 60
current_minute = total_minutes % 60
current_hour = (total_hours % 60) + 1

print(current_hour,':',current_minute,':',current_second)