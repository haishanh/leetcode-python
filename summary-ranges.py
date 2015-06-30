#!/usr/bin/env python

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        res = []
        stack = []
        new = []
        if len(nums) == 1:
            res.append([nums[0]])
        for i, e in enumerate(nums):
            if i == 0:
                stack.append(e)
                continue
            if e == nums[i-1] + 1:
                stack.append(e)
                if i == len(nums) - 1:
                    res.append(stack)
            else:
                res.append(stack)
                stack = [e]
                if i == len(nums) -1:
                    res.append(stack)
        # print("==>", res)
        for l in res:
            if len(l) >= 2:
                new.append(str(l[0]) + '->' + str(l[-1]))
            else:
                new.append(str(l[0]))
        return new


def test():
    s = Solution()
    nums = [0, 1, 2, 4, 5, 7]
    res = s.summaryRanges(nums)
    print(res)
    assert res == ['0->2', '4->5', '7']
    nums = [0]
    res = s.summaryRanges(nums)
    print(res)
    assert res == ['0']
    nums = [0, 1]
    res = s.summaryRanges(nums)
    print(res)
    assert res == ['0->1']
    nums = [-1]
    res = s.summaryRanges(nums)
    print(res)
    assert res == ['-1']

if __name__ == '__main__':
    test()
