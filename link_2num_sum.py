#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Chunyu Zhang
@license: 
@file: link_2num_sum.py
@time: 18/5/29 下午8:15
"""
'''
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

'''
本题比较简单,但最大的问题是一些边界条件的进位问题非常大,需要多关注,估计和大数加法差不多.
'''

# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution_v2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = []

        if not l1 and not l2:
            ret = []

        if not l1 and l2:
            ret = l2

        if l1 and not l2:
            ret = l1

        increment = 0
        min_len = min(len(l1),len(l2))
        for i in range(min_len):
            sum = l1.val + l2.val
            if sum >= 10:
                ret.append( sum % 10 + increment)
                increment = 1
            else:
                ret.append( sum + increment)
                increment = 0
        for i in range(min_len,len(l1)):
            ret.append(l1[i])
        for i in range(min_len,len(l2)):
            ret.append(l2[i])
        return ret

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)

        if not l1 and not l2:
            return None

        if not l1 and l2:
            ret = l2

        if l1 and not l2:
            ret = l1

        index = ret
        increment = 0
        while l1 is not None and l2 is not None:
            node_tmp = ListNode(0)
            sum = l1.val + l2.val + increment
            if sum >= 10:
                node_tmp.val = sum % 10
                increment = 1
            else:
                node_tmp.val = sum
                increment = 0
            index.next = node_tmp
            index = index.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            node_tmp = ListNode(0)
            sum = l1.val + increment
            if sum >= 10:
                node_tmp.val = sum % 10
            else:
                node_tmp.val = sum
                increment = 0
            index.next = node_tmp
            index = index.next
            l1 = l1.next
        while l2 is not None:
            node_tmp = ListNode(0)
            sum = l2.val + increment
            if sum >= 10:
                node_tmp.val = sum % 10
                increment = 1
            else:
                node_tmp.val = sum
                increment = 0
            index.next = node_tmp
            index = index.next
            l2 = l2.next
        if increment != 0:
            node_tmp = ListNode(0)
            node_tmp.val = increment
            increment =  0
            index.next = node_tmp
            index = index.next

        ret = ret.next
        return ret

