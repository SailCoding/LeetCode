# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:37:52 2019

@author: WW
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for index, num in enumerate(nums):
            numDiff = target - num
            if numDiff in numsMap.keys():
                return [index, numsMap[numDiff]]
            numsMap[num] = index
        return None
