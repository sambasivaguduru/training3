import threading
from time import sleep
c=0
lock=threading.Lock()
def fun():
	global c, lock
	print "validation done"
	print threading.current_thread()
	for i in range(5):
		lock.acquire()
		c=c+1
		print c
		lock.release()
		
t1=threading.Thread(target=fun, name="t1")
t2=threading.Thread(target=fun, name="t2")
t3=threading.Thread(target=fun, name="t3")
t1.start()
t2.start()
t3.start()
