from typing import List
def rec(num,num_index,queries,q_index,depth):
        if num==0:
            # print(f"yes: q_index:{q_index},depth:{depth}")
            return depth
        if q_index>=len(queries):
            return 100000
        if num<0:
            return 100000
        l=queries[q_index][0]
        r=queries[q_index][1]
        if not l<=num_index<=r:
             return rec(num,num_index,queries,q_index+1,depth+1)
        val=queries[q_index][2]
        ans1=rec(num-val,num_index,queries,q_index+1,depth+1)
        ans3=rec(num-val,num_index,queries,q_index,depth+1)
        ans2=rec(num,num_index,queries,q_index+1,depth+1)
        ans=min(ans1,ans2,ans3)
        # print(f"min_ans:{ans}, n:{num},num_index:{num_index}")
        return ans
        
        
def minZeroArray(nums: List[int], queries: List[List[int]]) -> int:
        ans=-100000000
        for i in range(len(nums)):
            ans=max(ans,rec(nums[i],i,queries,0,0))
            print(f"ans for i:{i} n:{nums[i]}:{ans}")
        if ans<=-100000000:
            return -1
        return ans

nums= [4,3,2,1]
queries= [[1,3,2],[0,2,1]]
output=3
print(minZeroArray(nums,queries))
