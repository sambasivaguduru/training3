from time import sleep
import threading
print threading.enumerate()
def fun1():
    for i in range(5):
        print threading.current_thread()

        print "hello world. 1 2 3 4 5 6 7 8 8 9 "
        
t1=threading.Thread(target=fun1, name="t1")
t2=threading.Thread(target=fun1, name="t2")
t3=threading.Thread(target=fun1, name="t3")
t1.start()
t2.start()
t3.start()