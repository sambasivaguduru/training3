import threading
from time import sleep
c=0
def fun():
	global c
	for i in range(5):
		c=c+1
		sleep(1)
		print c
t1=threading.Thread(target=fun, name="t1")
t2=threading.Thread(target=fun, name="t2")
t3=threading.Thread(target=fun, name="t3")
t1.start()
t1.join()
t2.start()
print "sdfdsf"
t2.join()
t3.start()
