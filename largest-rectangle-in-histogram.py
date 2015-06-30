#!/usr/bin/env python

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        tmp = height
        factor = 0
        res = 0
        while True in map(lambda x:x>0, tmp):
            num = 0
            _num = 0
            min_in_list = max(tmp)
            for i in tmp:
                if i > 0:
                    min_in_list = min(min_in_list, i)
                    num += 1
                    # print(".")
                    # print(num)
                else:
                    # print("-")
                    _num = max(_num, num)
                    num = 0
            _num = max(_num, num)
            factor += min_in_list
            _num *= factor
            tmp = map(lambda x:x-min_in_list, tmp)
            # factor += min_in_list
            res = max(_num, res)
        return res

def test():
    s = Solution()
    h = [2,1,5,6,2,3]
    x = s.largestRectangleArea(h)
    print(x)
    h = [0,0,0,0,0,0,0,0,214748]
    x = s.largestRectangleArea(h)
    print(x)


test()
