import threading
import time
from contextlib import contextmanager

class Resource:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()
    
    def __str__(self):
        return self.name

class DeadlockManager:
    def __init__(self):
        self.resources = {}
        self.resource_order = []
        self.timeout = 5
        self.global_lock = threading.Lock()
    
    def acquire_resources(self, required_resources):
        # Hierarchical Resource Ordering
        ordered_resources = sorted(required_resources, key=lambda x: self.resource_order.index(x.name))
        
        # Try to acquire all resources with timeout
        acquired = []
        try:
            for resource in ordered_resources:
                if not resource.lock.acquire(timeout=self.timeout):
                    # If timeout occurs, release all acquired resources
                    for acquired_resource in acquired:
                        acquired_resource.lock.release()
                    raise TimeoutError("Timeout while acquiring {}".format(resource))
                acquired.append(resource)
            return True
        except TimeoutError as e:
            print("Deadlock prevented: {}".format(e))
            return False

    def release_resources(self, resources):
        for resource in resources:
            resource.lock.release()

    @contextmanager
    def use_resources(self, *resources):
        try:
            if self.acquire_resources(resources):
                yield
        finally:
            self.release_resources(resources)

def simulate_deadlock():
    # Create resources
    resource_a = Resource("A")
    resource_b = Resource("B")
    
    def process_1():
        print("Process 1: Trying to acquire Resource A")
        resource_a.lock.acquire()
        print("Process 1: Acquired Resource A")
        
        # Simulate some work
        time.sleep(1)
        
        print("Process 1: Trying to acquire Resource B")
        resource_b.lock.acquire()
        print("Process 1: Acquired Resource B")
        
        # Release resources
        resource_b.lock.release()
        resource_a.lock.release()
    
    def process_2():
        print("Process 2: Trying to acquire Resource B")
        resource_b.lock.acquire()
        print("Process 2: Acquired Resource B")
        
        # Simulate some work
        time.sleep(1)
        
        print("Process 1: Trying to acquire Resource A")
        resource_a.lock.acquire()
        print("Process 2: Acquired Resource A")
        
        # Release resources
        resource_a.lock.release()
        resource_b.lock.release()
    
    # Create and start threads
    thread1 = threading.Thread(target=process_1)
    thread2 = threading.Thread(target=process_2)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

def demonstrate_deadlock_prevention():
    # Create resources and deadlock manager
    manager = DeadlockManager()
    resource_a = Resource("A")
    resource_b = Resource("B")
    
    # Set resource ordering
    manager.resource_order = ["A", "B"]
    
    def safe_process_1():
        print("Safe Process 1: Starting")
        with manager.use_resources(resource_a, resource_b):
            print("Safe Process 1: Acquired both resources")
            time.sleep(1)
        print("Safe Process 1: Released resources")
    
    def safe_process_2():
        print("Safe Process 2: Starting")
        with manager.use_resources(resource_a, resource_b):
            print("Safe Process 2: Acquired both resources")
            time.sleep(1)
        print("Safe Process 2: Released resources")
    
    # Create and start threads
    thread1 = threading.Thread(target=safe_process_1)
    thread2 = threading.Thread(target=safe_process_2)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    print("Simulating deadlock...")
    simulate_deadlock()
    
    print("\nDemonstrating deadlock prevention...")
    demonstrate_deadlock_prevention()