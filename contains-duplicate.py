#!/usr/bin/env python

# time exceeded
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        for i,e in enumerate(nums):
            if e in nums[i+1:]:
                return True
        return False

class Solution2:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)

# runtime -> 60ms
class Solution3:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        d = {}
        for e in nums:
            if e in d:
                return True
            else:
                d[e] = 1
        return False

def test():
    s = Solution3()
    assert True == s.containsDuplicate([1,2,3,4,4,5,6])
    assert False == s.containsDuplicate([1,2,3])
    assert True == s.containsDuplicate([1,1,2])
    assert True == s.containsDuplicate([1,2,3,4,5,6,2,7,8])
    assert False == s.containsDuplicate([9,6,2,4,1,3])
    long_list = range(10000000)
    long_list.append(9)
    assert True == s.containsDuplicate(long_list)
    print('Test Passed!')

if __name__ == '__main__':
    test()
