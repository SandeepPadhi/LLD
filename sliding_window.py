"""
We will be doing sliding window:
1. sum
2. avg
3. max
4. min

"""
from collections import deque

class SlidingWindow:
    def __init__(self,window_size,arr):
        self.window_size=window_size
        self.input_arr=arr
        self.sum_arr=[]
        self.avg_arr=[]
        self.max_arr=[]
        self.min_arr=[]
        self._process()

    def sliding_sum(self):
        current_sum=0
        for index,element in enumerate(self.input_arr):
            current_sum+=element
            if index>=self.window_size:
                current_sum-=self.input_arr[index-self.window_size]
            if index>=self.window_size-1:
                self.sum_arr.append(current_sum)
    
    def sliding_avg(self):
        current_sum=0
        for index,element in enumerate(self.input_arr):
            current_sum+=element
            if index>=self.window_size:
                current_sum-=self.input_arr[index-self.window_size]
            if index>=self.window_size-1:
                self.avg_arr.append(current_sum/self.window_size)
    
    def sliding_max(self):
        dq=deque()
        for index,element in enumerate(self.input_arr):
            while dq and index-dq[0]>=self.window_size:
                dq.popleft()

            while dq and self.input_arr[dq[-1]]<=element:
                dq.pop()

            dq.append(index)
            if dq and index>=self.window_size-1:
                self.max_arr.append(self.input_arr[dq[0]])

    def sliding_min(self):
        dq=deque()
        for index, element in enumerate(self.input_arr):
            while dq and index-dq[0]>=self.window_size:
                dq.popleft()

            while dq and dq[-1]>=element:
                dq.pop()

            dq.append(index)
            if dq and index>=self.window_size-1:
                self.min_arr.append(self.input_arr[dq[0]])


    def _process(self):
        # self.sliding_sum()
        # self.sliding_avg()
        self.sliding_max()
        self.sliding_min()
    
def app():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    window_size=4
    sliding_window=SlidingWindow(window_size,nums)
    print(f"sum arr:{sliding_window.sum_arr}")
    print(f"avg arr:{sliding_window.avg_arr}")
    print(f"max arr:{sliding_window.max_arr}")
    print(f"max arr:{sliding_window.min_arr}")





if __name__ == "__main__":
    app()
        
                
            
        


        



