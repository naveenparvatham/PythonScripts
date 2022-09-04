import time

my_time = time.localtime()
if my_time.tm_hour < 6 or my_time.tm_hour > 18:
    print('It is night-time')
else:
    print('It is day-time')
