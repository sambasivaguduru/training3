from time import sleep
import threading
print threading.enumerate()
def fun1():
	for i in range(5):
	    sleep(1)
	    print i
for i in range(3):
	fun1()