#!/usr/bin/env python

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = ''
        tmp = n
        while tmp:
            s = str(tmp % 2) + s
            tmp //= 2
        res = 0
        #.padding
        # s = (32 - len(s)) * '0' + s
        # factor = 1

        #.the following line is just like padding above
        #.but should be slightly faster
        factor = 2 ** (32 - len(s))
        # from LSB to MSB
        for i in s:
            if i == '1':
                res += factor
            factor *= 2
        return res

def test():
    s = Solution()
    assert 964176192 == s.reverseBits(43261596)
    assert 2147483648 == s.reverseBits(1)
    print('Test passed!')

if __name__ == '__main__':
    test()
