#!/usr/bin/env python

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        # reduce the list
        while nums[0] + nums[1] + nums[2] + nums[-1] > target:
            nums.pop(-1)
        for i,num in enumerate(nums):
            if num >= target // 4:
                anch = i
        for i in nums[:anch]:
            for j in nums[anch:]:
                if i + j >= target






