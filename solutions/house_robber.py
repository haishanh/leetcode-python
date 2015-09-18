#!/usr/bin/env python

#TODO

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        even_sum, odd_sum = 0, 0
        for i,e in enumerate(nums):
            if i % 2 == 0:
                even_sum += e
            else:
                odd_sum += e
        return max(even_sum, odd_sum)

class Solution2:
    def rob(self, nums):
        last, now = 0, 0
        for i in nums: last, now = now, max(last + i, now)
        return now

def test():
    s = Solution2()
    n = [1,2,3,4]
    print(s.rob(n))
    assert 1100 == s.rob([100, 1, 2, 1000, 3])
    assert 14 == s.rob([1, 5, 10, 9, 2])


if __name__ == '__main__':
    test()
