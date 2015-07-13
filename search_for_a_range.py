#!/usr/bin/env python
from __future__ import print_function

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if target not in nums:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            num = nums[mid]
            if num == target:
                break
            elif num > target:
                end = mid - 1
            else:
                start = mid + 1
        # bi-direaction seach
        for i in range(mid, len(nums)):
            if nums[i] != target:
                break
            end = i
        i = mid
        while i >= 0:
            if nums[i] != target:
                break
            start = i
            i -= 1
        return [start, end]


def test():
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    assert [3, 4] == s.searchRange(nums, 8)
    assert [0, 0] == s.searchRange(nums, 5)
    assert [5, 5] == s.searchRange(nums, 10)
    nums = [3, 4]
    assert [0, 0] == s.searchRange(nums, 3)
    assert [1, 1] == s.searchRange(nums, 4)
    assert [-1, -1] == s.searchRange(nums, 6)
    nums = [1,2,3]
    assert [1,1] == s.searchRange(nums, 2)
    print('Test passed!')

if __name__ == '__main__':
    test()
