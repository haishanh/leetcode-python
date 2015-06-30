#!/usr/bin/env python

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        def cal_cover(x0,y0,x1,y1):
            total = y0 - x0 + y1 -x1
            if x1 >= x0:
                total = total - x1 + x0
            else:
                total = total - x0 + x1
            if y1 >= y0:
                total = total - y1 + y0
            else:
                total = total - y0 + y1
            if total > 0:
                total /= 2
            else:
                # these two rectangles do not overlap
                total = 0
            return total
        w = cal_cover(A, C, E, G)
        h = cal_cover(F, H, B, D)
        all = (C-A) * (D-B) + (G-E) * (H-F)
        return all - w * h

def test():
    s = Solution()
    assert 45 == s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
    assert 17 == s.computeArea(-2, -2, 2, 2, 3, 3, 4, 4)
    assert 4  == s.computeArea(0, 0, 0, 0, -1, -1, 1, 1)
    print('Test Passed!')

if __name__ == '__main__':
    test()
