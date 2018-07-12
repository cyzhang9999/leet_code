#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Chunyu Zhang
@license: 
@file: jump_game.py
@time: 18/6/7 下午10:04
"""

class Solution(object):
    '''
    自己写的这个版本卡在第73个测试用例上,会超时. 还是理解的不够好.
    '''

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        record = []
        for i in range(len(nums)):
            record_tmp =  []
            for j in range(len(nums)):
                record_tmp.append(0)
            record.append(record_tmp)
        return self.re_can_jump(nums,len(nums)-2,record)

    def re_can_jump(self,nums,n,record):
        n_re = n
        if n < 0:
            return True
        while n >= 0:
            if record[n_re][n] != 0:
                return record[n_re][n]
            if nums[n] >= n_re - n + 1:
                record[n_re][n] = True
                ret_tmp = self.re_can_jump(nums,n_re-1,record)
                #if ret_tmp :
                return ret_tmp
            else:
                record[n_re][n] = False
            n -= 1
        return False

class Solution1(object):
    '''
    抄一个DP的写法,还不是最优的,最优的是贪婪算法. 简洁不少,效率更高,这个DP问题的抽象还需要强化.

    这道题说的是有一个非负整数的数组，每个数字表示在当前位置的基础上最多可以走的步数，求判断能不能到达最后一个位置，开始我以为是必须刚好到达最后一个位置，超过了不算，其实是理解题意有误，因为每个位置上的数字表示的是最多可以走的步数而不是像玩大富翁一样摇骰子摇出几一定要走几步。那么我们可以用动态规划Dynamic Programming来解，我们维护一个一位数组dp，其中dp[i]表示达到i位置时剩余的步数，那么难点就是推导状态转移方程啦。我们想啊，到达当前位置的剩余步数跟什么有关呢，其实是跟上一个位置的剩余步数和上一个位置的跳力有关，这里的跳力就是原数组中每个位置的数字，因为其代表了以当前位置为起点能到达的最远位置。所以当前位置的剩余步数（dp值）和当前位置的跳力中的较大那个数决定了当前能到的最远距离，而下一个位置的剩余步数（dp值）就等于当前的这个较大值减去1，因为需要花一个跳力到达下一个位置，所以我们就有状态转移方程了：dp[i] = max(dp[i - 1], nums[i - 1]) - 1，如果当某一个时刻dp数组的值为负了，说明无法抵达当前位置，则直接返回false，最后我们判断dp数组最后一位是否为非负数即可知道是否能抵达该位置
    '''

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        record = [0 for i in range(len(nums))]

        for i in range(1,len(nums)):
            record[i] = max(record[i-1],nums[i-1])-1
            if record[i]<0:
                return False
        return record.pop() >= 0

class Solution2(object):
    '''
    这题最好的解法不是DP，而是贪婪算法Greedy Algorithm，因为我们并不是很关心每一个位置上的剩余步数，我们只希望知道能否到达末尾，也就是说我们只对最远能到达的位置感兴趣，所以我们维护一个变量reach，表示最远能到达的位置，初始化为0。遍历数组中每一个数字，如果当前坐标大于reach或者reach已经抵达最后一个位置则跳出循环，否则就更新reach的值为其和i + nums[i]中的较大值，其中i + nums[i]表示当前位置能到达的最大位置
    '''

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        length = len(nums)
        for i in range(length):
            if i <= reach:
                reach = max(reach,i+nums[i])
            elif i > reach:
                return False
            if reach >= length-1:
                return True

if __name__ == "__main__":
    test1 = [2,3,1,1,4]
    test2 = [1,2,1,0,2,1,2,1,0]
    so = Solution2()
    print so.canJump(test1)
    print so.canJump(test2)

