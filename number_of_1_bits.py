#!/usr/bin/env python

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        tmp = n
        count = 0
        while tmp:
            if tmp % 2 == 1:
                count += 1
            tmp //= 2
        return count

def test():
    s = Solution()
    assert 3 == s.hammingWeight(11)
    assert 1 == s.hammingWeight(2)
    assert 0 == s.hammingWeight(0)
    print('Test passed!')

if __name__ == '__main__':
    test()
