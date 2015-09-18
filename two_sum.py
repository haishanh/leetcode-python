#!/usr/bin/env python

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return d[target - num] + 1, i + 1
            d[num]=i

def test():
    s = Solution()
    nums = [2, 7, 11, 15,]
    target = 9
    print(s.twoSum(nums, target))

test()
