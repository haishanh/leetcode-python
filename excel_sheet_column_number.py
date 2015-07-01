#!/usr/bin/env python

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        count = 0
        factor = 1
        for i, c in enumerate(s[::-1]):
            x = ord(c) - ord('A') + 1
            x *= factor
            factor *= 26
            count += x
        return count

def test():
    s = Solution()
    assert 1 == s.titleToNumber('A')
    assert 2 == s.titleToNumber('B')
    assert 26 == s.titleToNumber('Z')
    assert 27 == s.titleToNumber('AA')
    print('Test passed!')

if __name__ == '__main__':
    test()
