# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 21:48:26 2019

@author: WW
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < numRows or numRows == 1:
            return s
        
        res = ''
        for i in range(numRows) :
            cur, l, r = i, 2 * (numRows - 1 - i), 2 * i
            res += s[cur]
            while True :
                if l != 0:
                    cur += l
                    if cur < len(s):
                        res += s[cur]
                    else:
                        break
                if r != 0:
                    cur += r
                    if cur < len(s):
                        res += s[cur]
                    else:
                        break
        return res
