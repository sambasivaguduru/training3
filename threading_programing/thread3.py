import threading
from time import sleep
dirt_alive = True
def dir_restart():
    global dirt_alive
    for i in range(5):
        sleep(1)
        print "restarting directory"
    dirt_alive=False
def io():
    global dirt_alive
    while True:
        sleep(1)
        print "passing io"
        if dirt_alive:
            continue
        else:
            break
dirt = threading.Thread(target=dir_restart)
io=threading.Thread(target=io)
dirt.start()
io.start()
print "program ended"