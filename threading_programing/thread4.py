import threading
from time import sleep
def dir_restart():
    for i in range(5):
        sleep(1)
        print "restarting directory"
    dirt_alive=False
def io():
    while True:
        sleep(1)
        print "passing io"
        if dirt.is_alive():
            continue
        else:
            break
dirt = threading.Thread(target=dir_restart)
io=threading.Thread(target=io)
io.start()
sleep(2)
dirt.start()

print "program ended"