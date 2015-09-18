#!/usr/bin/env python
from __future__ import print_function
import random


# runtime ~72ms on leetcode.com
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        if k > len(nums):
            k -= len(nums)
        tmp = nums[-k:]
        nums[:] = tmp + nums[:-k]

# runtime ~208ms on leetcode.com
class Solution2:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        if k > len(nums):
            k -= len(nums)
        for i in range(k):
            nums.insert(0, nums.pop())

def test_case(solution):
    def do_and_prt(nums, k):
        print('Before rotate %d steps:' % (k), nums)
        solution.rotate(nums, k)
        print('After  rotate %d steps:' % (k), nums)

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    do_and_prt(nums, k)
    nums = [1, 2]
    k = 3
    do_and_prt(nums, k)

def test():
    s = Solution()
    test_case(s)

if __name__ == '__main__':
    test()
