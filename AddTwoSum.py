# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:38:43 2019

@author: WW
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        res = ListNode(0)
        head = res
        while l1 and l2 :
            tmp = l1.val + l2.val + carry
            carry = tmp // 10
            tmp = tmp % 10
            head.next = ListNode(tmp)
            head = head.next
            l1 = l1.next
            l2 = l2.next
            
        maxL = l1 if l1 else l2
        while maxL :
            tmp = carry + maxL.val
            carry = tmp // 10
            tmp = tmp % 10
            head.next = ListNode(tmp)
            head = head.next
            maxL = maxL.next
            
        if carry > 0 :
            head.next = ListNode(carry)
            head = head.next
        
        return res.next
            