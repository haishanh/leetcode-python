#!/usr/bin/env python

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        count = 0
        for i, c in enumerate(s[::-1]):
            x = ord(c) - ord('A') + 1
            factor = 26 ** i
            x = x * factor
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
