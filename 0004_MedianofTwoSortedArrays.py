# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 23:43:02 2019

@author: WW
"""

'''
A[0], A[1], ... , A[i-1], | A[i], ... , A[m]
B[0], B[1], ... , B[j-1], | B[j], ... , B[n]
A[i-1] <= B[j] && B[j-1] <= A[i]
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        if m < n :
            nums1, nums2 = nums2, nums1
            m, n = n, m
        
        iMin, iMax, halfLen = 0, m, (m+n+1)//2
        while iMin <= iMax:
            i = (iMin + iMax) // 2
            j = halfLen - i
            if i < m and nums2[j-1] > nums1[i]:
                print('--', j ,i)
                iMin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                iMax = i - 1
                print('++', j, i)
            else :
                if i == 0:
                    maxLeft = nums2[j-1]
                elif j == 0: 
                    maxLeft = nums1[i-1]
                else:
                    maxLeft = max(nums2[j-1], nums1[i-1])
                    
                if (m+n) % 2 == 1:
                    return maxLeft
                
                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                
                return (maxLeft + minRight) / 2.0
                    
        
        
                    
                    
s = Solution()
res = s.findMedianSortedArrays([1, 2], [3])
print(res)