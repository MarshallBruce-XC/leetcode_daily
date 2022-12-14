# -*- coding: utf-8 -*-
'''
# Created on 09-17-22 17:39
# @Filename: 1_twoSum.py
# @Desp: 来源于https://leetcode.cn/problems/two-sum
# @software: vscode
# @author: xuchang0514@sina.com
'''
#lib moduls:
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from typing import List

# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

# 示例 2：
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]

# 示例 3：
# 输入：nums = [3,3], target = 6
# 输出：[0,1]

# 提示：
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 只会存在一个有效答案

# 进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = []

        for i,n in enumerate(nums):
            # if n <= target:
            try:
                another = nums.index(target-n)
            except:
                continue
            if i != another:
                res = [i,another]
                break

        return res

nums = [-1,-2,-3,-4,-5]
t = -8

s = Solution()
print(s.twoSum(nums,t))