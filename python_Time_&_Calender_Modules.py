import calendar
yy = 1994
mm = 2
print (calendar.month(yy, mm))

#      or

print (calendar.month(1994, 2))

import time
print (time.time())
print (time.localtime(time.time()))
print (time.asctime(time.localtime(time.time())))
