#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: Chunyu Zhang
@license: 
@file: phone_num_combine.py
@time: 18/5/31 下午10:06
"""

'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution(object):
    num_mapping = {
        "2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"],
    }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = []
        if digits and len(digits)>0:
            cur_arr = []
            for i in range(len(digits)):
                cur_arr.append("0")
            self.combine_num(digits,0,len(digits)-1,ret,cur_arr)

        return ret

    def combine_num(self,digits,i,n,ret,cur_arr):
        char_arr = Solution.num_mapping[digits[i]]
        for each_char in char_arr:
            cur_arr[i] = each_char
            if i == n:
                ret.append("".join(cur_arr))
            else:
                self.combine_num(digits,i+1,n,ret,cur_arr)

if __name__ == "__main__":
    so =  Solution()
    ret = so.letterCombinations("23")
    print str(ret)