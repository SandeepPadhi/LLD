
import threading
from typing import List
from enum import Enum
import time

class Resource:
    def __init__(self, name):
        self.name=name
        self.lock=threading.Lock()
    
    def __str__(self):
        return self.name

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

class DeadlockManager:
    def __init__(self):
        self.timeout=5 
        self.resource_acquired=[]
        self.resourceorder=[]

    def acquire_lock(self,resources:List[Resource]):
        resources=sorted(resources,key=lambda x:self.resourceorder.index(x.name))
        for resource in resources:
            try:
                if not resource.lock.acquire(timeout=self.timeout):
                    print("releasing lock as unable to acquire for {}".format(resource))
                    self.release_lock(self.resource_acquired)
                    raise TimeoutError("unable to acquire lock for resource:{}".format(resource))
                print("lock acquired successully for resource:{}".format(resource))    
                self.resource_acquired.append(resource)
            except TimeoutError as t:
                return False 
        self.release_lock(resources)
        return True

    def release_lock_all(self):
        print("releasing all locks:{}".format(self.resource_acquired))
        for resource in self.resource_acquired:
            resource.lock.release()
            self.resource_acquired.remove(resource)
            print("lock released successfully for resource:{}".format(resource))

    def release_lock(self,resources):
        resources=sorted(resources,key=lambda x:self.resourceorder.index(x.name))
        for resource in resources:
            if resource in self.resource_acquired:
                print("releasing locks for resource:{}".format(resource))
                self.resource_acquired.remove(resource)
        

            
def handle_deadlock():
    print("calling handle_deadlock")
    manager=DeadlockManager()
    resource1=Resource('A')
    resource2=Resource('B')

    manager.resourceorder=['B','A']
    

    def safe_process1():
        if not manager.acquire_lock([resource2,resource1]):
            print("unable to acquire lock for safe_process1")
            return False
    
    def safe_process2():
        if not manager.acquire_lock([resource1,resource2]):
            print("unable to acquire lock for safe_process2")
            return False

    t1=threading.Thread(target=safe_process1)
    t2=threading.Thread(target=safe_process2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    manager.release_lock_all()





def simulate_deadlocks():
    resource1=Resource('A')
    resource2=Resource('B')
    to=5
    print(resource1)
    print(resource2)

    def process1(r1:Resource,r2:Resource):
        v=resource1.lock.acquire(timeout=5)
        if not v:
            print("Could not acquire lock:{}".format(resource1))
            return
        print("process1:lock {} acquired".format(r1))
        time.sleep(1)
        v=resource2.lock.acquire(timeout=10)
        if not v:
            print("Could not acquire lock:{}".format(resource2))
            resource1.lock.release()
            return

        print("process1: lock {} acquired".format(r2))
        resource2.lock.release()
        print("process1: lock {} released".format(r2))
        resource1.lock.release()        
        print("process1: lock {} released".format(r1))


    def process2(r1:Resource,r2:Resource):
        v=resource2.lock.acquire(timeout=5)
        if not v:
            print("Could not acquire lock:{}".format(resource2))
            return

        print("process2: lock {} acquired".format(r2))
        time.sleep(1)
        v=resource1.lock.acquire(timeout=5) 
        if not v:
            print("Could not acquire lock:{}".format(resource1))
            resource2.lock.release()
            return

        print("process2: lock {} acquired".format(r1))
        resource1.lock.release()
        print("process2: lock {} released".format(r1))
        resource2.lock.release()
        print("process2 : lock {} released".format(r2))

            

    t1 = threading.Thread(target=process1,args=(resource1, resource2))
    t2 = threading.Thread(target=process2,args=(resource1, resource2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def main():
    print("Simulating deadlocks")
    simulate_deadlocks()

    print(Direction.EAST.value)
    print(Direction.NORTH)


    handle_deadlock()
    



main()





