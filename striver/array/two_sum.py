"""
Date:17/03/2025
Link: https://leetcode.com/problems/two-sum/description/
"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp={}
        for i in range(len(nums)):
            n=nums[i]
            if target-n in dp:
                return [i,dp[target-n]]
            if n not in dp:
                dp[n]=i 
        return [-1,-1]