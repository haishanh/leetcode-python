#!/usr/bin/env python

class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        # ord('A') == 65
        tmp = n
        s = ''
        while tmp:
            x = (65 + tmp % 26 - 1)
            if x == 64:
                s = 'Z' + s
                tmp -= 1
            else:
                s = chr(x) + s
            tmp = tmp // 26
        return s

def test():
    s = Solution()
    assert 'A' == s.convertToTitle(1)
    assert 'C' == s.convertToTitle(3)
    assert 'Z' == s.convertToTitle(26)
    assert 'AB' == s.convertToTitle(28)
    assert 'AY' == s.convertToTitle(51)
    assert 'AZ' == s.convertToTitle(52)
    print('Test passed!')


if __name__ == '__main__':
    test()
