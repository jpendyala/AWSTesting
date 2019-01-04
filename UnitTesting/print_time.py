# Python code to demonstrate the working of
# time() and gmtime()
from __future__ import absolute_import, division, print_function
#  importing "time" module for time operations
import time

# using time() to display time since epoch
print ("Current Time is : ", end="")


for x in range(6):
    print( time.strftime('%X %x %Z') )
    time.sleep(1)
