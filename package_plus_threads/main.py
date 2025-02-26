from threads import Threads
from queue import Queue
from threading import Lock

def main():
    q=Queue()
    l=Lock()
    t1=Threads(1,q,l)
    t2=Threads(2,q,l)
    q.put(1)
    q.put(2)
    q.put("done")
    q.put("done")
    print("done yaar")
    q.task_done()
    q.task_done()
    q.task_done()
    q.task_done()
    q.join()
    print("now done")



if __name__ == "__main__":
    main()