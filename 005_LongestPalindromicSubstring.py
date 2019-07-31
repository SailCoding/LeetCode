# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 23:22:11 2019

@author: WW
"""

"""
1.暴力法
    isPalindrome = lamdba s: s == s[::-1]
2.中心法
3.动态规划
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxIndex, maxLen = 0, 0
        for i in range(len(s)):
            startIndex, curLen = self.expend(s, i, i)
            if curLen > maxLen:
                maxIndex = startIndex
                maxLen = curLen
            startIndex, curLen = self.expend(s, i, i+1)
            if curLen > maxLen:
                maxIndex = startIndex
                maxLen = curLen
        return s[maxIndex:maxIndex+maxLen]
    
    def expend(self, s, left, right):
        startIndex, curLen = 0, 0
        
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                curLen = right - left + 1
                startIndex = left
            else :
                return startIndex, curLen
            left -= 1
            right += 1
            
        return startIndex, curLen
        
        

s = Solution();
res = s.longestPalindrome("babad")
print(res)
res = s.longestPalindrome('a')
print(res)
res = s.longestPalindrome('aa')
print(res)