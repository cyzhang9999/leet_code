#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Chunyu Zhang
@license: 
@file: 3numbs.py
@time: 18/5/28 下午9:45
"""

'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组
'''

'''
记录: 这里有4个版本:
1. 自己写的暴力解决方法,用递归的.
2. 参考别人的,排序后,现找一个数,然后查找后两个数,然后用dict去重
3. 再次参考别人的,利用排序的规律去重,在311过不了,超时
4. 纯粹别人的,
 3和4的思路是一致的,但4能过,3过不了,可见leetcode卡的非常严,一些小的编程习惯也会被影响.

 最后找到了是因为3有一个地方写错了.
'''

class Solution(object):
    def __init__(self):
        self.record = [0,0,0]
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = {}
        self.re_find(nums,0,len(nums),0,ret)
        return ret.values()

    def re_find(self,numbs,b,e,n,ret):
        if n == 2:
            for i in range(b,e):
                self.record[n] = numbs[i]
                self.can_be_record(ret)
        elif n<2:
            for i in range(b,e):
                self.record[n] = numbs[i]
                self.re_find(numbs,i+1,e,n+1,ret)

    def can_be_record(self,ret):
        sum = self.record[0]+self.record[1]+self.record[2]
        if sum == 0:
            sort = sorted(self.record)
            key = "".join([str(each) for each in sort])
            if not ret.has_key(key):
                ret[key] = sort
            return True
        else:
            return False

class Solution_v2(object):
    def __init__(self):
        pass
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = {}
        if nums and len(nums)>0:
            sort_nums = sorted(nums)
            #print sort_nums
            for i in range(len(sort_nums)):
                if sort_nums[i] <= 0 :
                    num2_arr = self.find_2num(sort_nums,i+1,len(sort_nums)-1,sort_nums[i] * -1,sort_nums[i],ret)
                    #if num2_arr and len(num2_arr)==2:
                        #num2_arr.insert(0,sort_nums[i])
                    #    ret.append(num2_arr)
                else:
                    break
        return ret.values()

    def find_2num(self,nums,b,e,n_to_find,begin_num,ret):
        ret_tmp = []
        i = 0
        b_record = b
        while b < e:
            #print b,e,n_to_find
            sum = nums[b] + nums[e]
            #print sum
            if sum == n_to_find:
                ret_tmp.append(begin_num)
                ret_tmp.append(nums[b])
                ret_tmp.append(nums[e])
                self.can_be_record(ret_tmp,ret)
                ret_tmp = []
                b = b_record
                e -= 1
            elif sum < n_to_find:
                b +=1
            elif sum > n_to_find:
                e -=1
            i += 1
        return ret

    def can_be_record(self,ret_tmp,ret):
        key = "".join([str(each) for each in ret_tmp])
        if not ret.has_key(key):
            ret[key] = ret_tmp


class Solution_v3(object):
    def __init__(self):
        pass
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if nums and len(nums)>0:
            nums.sort()
            #print nums
            length= len(nums)
            for i in range(length):
                if nums[i] <= 0 :
                    if i > 0 and nums[i]== nums[i-1]:
                        continue
                    b = i+1
                    e = length -1
                    n_to_find = 0 - nums[i]
                    while b < e:
                        sum = nums[b] + nums[e]
                        if sum == n_to_find:
                            ret.append([nums[i],nums[b],nums[e]])
                            b = +1 ##写了一个错误,造成每次都是从1开始,浪费时间了
                            e -= 1
                            while (b<e and nums[b]==nums[b-1]): b+=1
                            while (b<e and nums[e]==nums[e+1]): e-=1
                        elif sum < n_to_find:
                            b +=1
                        else:
                            e -=1
                else:
                    break
        return ret
    
class Solution_v4(object):
    def __init__(self):
        pass
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        count = len(nums)
        collect = []
        for i in range(count):
            left = i+1
            right = count-1
            #避免重复找同一个数据
            if i >0 and nums[i] == nums[i-1]:
                left +=1
                continue
            #数据按小到大排列，每次选取nums[i]，在其后寻找符合a + b + c = 0的两个数据
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    col = [nums[i],nums[left],nums[right]]
                    collect.append(col)
                    left+=1
                    right-=1
                    #循环中nums[i]已确定，当再确定1个数时，另一个数也确定，左右端任一端出现重复均可跳过
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                    while nums[right] == nums[right+1] and left < right:
                        right-=1
                if sum<0:
                    left+=1
                elif sum > 0:
                    right-=1
        return collect

if __name__ == '__main__':
    test = [-1,0,1,2,-1,-4]
    solution = Solution_v3()
    ret = solution.threeSum(test)
    print ret
