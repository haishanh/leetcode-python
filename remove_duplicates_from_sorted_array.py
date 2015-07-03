#!/usr/bin/env python

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        prev = ''
        i = 0
        j = 0
        # ori_len = len(nums)
        for i in range(len(nums)):
            curr = nums[i]
            if curr != prev:
                nums[j] = curr
                j += 1
            prev = curr
        #.if we really want in-place
        #.we might need some nums.pop() here, like below
        # for i in range(ori_len - j):
        #     nums.pop()
        return j

def test():
    s = Solution()
    n = [1, 1, 2]
    assert 2 == s.removeDuplicates(n)
    # assert n == [1, 2]
    n = [1, 2, 3]
    assert 3 == s.removeDuplicates(n)
    # assert n == [1, 2, 3]
    n = [1, 1, 1]
    assert 1 == s.removeDuplicates(n)
    # assert n == [1]
    print('Test passed!')


if __name__ == '__main__':
    test()
