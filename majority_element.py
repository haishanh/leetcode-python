#!/usr/bin/env python

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        d = {}
        for i in nums:
            if d.get(i):
                d[i] += 1
            else:
                d[i] = 1
        half = len(nums) // 2
        for i in d.keys():
            if d[i] > half:
                return i


class Solution2:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

def test():
    s = Solution()
    assert 3 == s.majorityElement([3, 1, 3, 1, 3])
    assert 4 == s.majorityElement([4, 1, 4, 4, 1, 4, 3, 4])
    print('Test passed!')


if __name__ == '__main__':
    test()
