from queue import Queue
from threading import Thread,Lock

class Threads:
    def __init__(self,no:int,q:Queue,lock:Lock):
        self.queue=q
        self.lock=lock
        self.no=no
        t=Thread(target=self.readInf)
        t.start()

    def readInf(self):
        while True:
            print("thread:{} waiting to acquire lock".format(self.no))
            with self.lock:
                print("acquired lock here in thread:{}".format(self.no))
                v=self.queue.get()
                print("thread:{} , value in the queue is:{}".format(self.no,v))
                if v=="done":
                    print("returning")
                    return 

