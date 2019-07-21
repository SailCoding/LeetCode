# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:05:45 2019

@author: WW
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int :
        left, right, res = 0, 0, 0
        chars = set()
        while right < len(s):
            if s[right] in chars:
                if s[left] in chars:
                    chars.remove(s[left])
                left += 1
            else:
                chars.add(s[right])
                res = max(res, len(chars))
                right += 1
        return res
    
    def lengthOfLongestSubstring1(self, s: str) -> int :
        l, res = 0, 0
        chars = dict()
        for r, value in enumerate(s) :
            if value in chars :
                l = max(l, chars[value] + 1)
            chars[value] = r
            res = max(res, r - l + 1)
        return res
    
s = Solution()
res = s.lengthOfLongestSubstring1('abcabcbb')
print(res)