#!/usr/bin/env python

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        if not height:
            return 0
        if len(height) == 1:
            return height[0]
        stack = []  # The bottom element in the stack is the lowest
        max_area = 0
        n = len(height)
        for i in range(n + 1):
            while stack and (i == n or height[stack[-1]] > height[i]):
                h = height[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                max_area = max(max_area, h * w)
                print(i, stack, max_area)
            stack.append(i)
        return max_area

def test():
    s = Solution()
    h = [2,1,5,6,2,3]
    x = s.largestRectangleArea(h)
    print(x)
    h = [2,1,5,6,2,3,2,2]
    x = s.largestRectangleArea(h)
    print(x)
    h = [0,0,0,0,0,0,0,0,214748]
    x = s.largestRectangleArea(h)
    print(x)


test()
