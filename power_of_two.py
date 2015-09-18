#!/usr/bin/env python

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n != n // 2 * 2:
            return False
        i = 1
        while i < n:
            i *= 2
        return i == n


def test():
    s = Solution()
    assert True == s.isPowerOfTwo(1024)
    assert False == s.isPowerOfTwo(1023)
    print('Test passed!')


if __name__ == '__main__':
    test()
