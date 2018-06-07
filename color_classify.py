#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Chunyu Zhang
@license: 
@file: color_classify.py
@time: 18/6/4 下午8:36
"""

'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
'''

'''
Solution 是优化解法,28ms
solution1 是常规解法,40ms
优化解法还是抄来的,这个交换过程,尤其1怎么处理,没想明白,交换过程倒是想到了,多练练吧
'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        b = 0
        e = len(nums)-1
        i = 0
        while i <= e :
            print nums[i]
            if nums[i] == 1:
                i +=1
            elif nums[i] == 2:
                self.swap(nums,i,e)
                e -= 1
            else:
                if nums[i] == 0:
                    self.swap(nums,i,b)
                    b += 1
                    i += 1

    def swap(self,arr,i1,i2):
        tmp = arr[i1]
        arr[i1] = arr[i2]
        arr[i2] = tmp

class Solution1(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #ret = nums
        n1 = [0,0,0]
        for each in nums:
            n1[each] += 1
        #print str(n1)

        for i in range(len(nums)):
            if i < n1[0]:
                nums[i] = 0
            if i >= n1[0] and i < n1[1]+n1[0]:
                nums[i] = 1
            if i >= n1[1]+n1[0]:
                nums[i] = 2
        #return ret

if __name__ == '__main__':
    so = Solution()
    #test = [2,0,2,1,1,0]
    test = [2,0,1]
    so.sortColors(test)
    print str(test)