#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Chunyu Zhang
@license: 
@file: tree_inorder_norecursive.py
@time: 18/5/30 下午9:22
"""
'''
简单吧,没写过一样转不过弯来.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root:
            stack = []
            cur_node = root
            while cur_node or len(stack)>0:
                while cur_node:
                    stack.append(cur_node)
                    cur_node = cur_node.left

                if len(stack)>0:
                    cur_node = stack.pop()
                    ret.append(cur_node.val)
                    cur_node = cur_node.right
        return ret