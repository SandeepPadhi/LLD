


import threading
from collections import deque
import time
import unittest

class RateLimiter:
    def __init__(self,limit,window_second):
        self.limit=limit 
        self.window_second=window_second
        self.user_request={}
        self.lock=threading.Lock()
    
    def allow_request(self,user_id):
        
        with self.lock:
            if user_id not in self.user_request:
                self.user_request[user_id]=deque()

            user_queue=self.user_request[user_id]
            current_time=time.time()
            while user_queue and user_queue[0]<current_time - self.window_second:
                user_queue.popleft()
            
            if len(user_queue)<self.limit:
                user_queue.append(current_time)
                return True 
            return False


def simulate_reuest(user_id,rate_limiter):
    if rate_limiter.allow_request(user_id):
        print(f"request is allowed for {user_id}")
    else:
        print(f"request is not allowed for {user_id}")

limit=3
window_second=5
rate_limiter=RateLimiter(limit,window_second)
user_id='user_id'

def run_request():
    threads=[]
    for i in range(10):
        t=threading.Thread(target=simulate_reuest,args=(user_id,rate_limiter,))
        t.start()
        time.sleep(1)

    for t in threads:
        t.join()

class TestRateLimiter(unittest.TestCase):
    def testratelimiter(self):
        run_request()
        self.assertTrue(len(rate_limiter.user_request[user_id])<=rate_limiter.limit)


if __name__ == '__main__':
    unittest.main()