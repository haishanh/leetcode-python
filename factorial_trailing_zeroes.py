#!/usr/bin/env python
# No.172

class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        if n < 5:
            return 0
        a = n
        count = 0
        i = 5
        while i <= a:
            count += n // i
            i *= 5
        return count

def test():
    s = Solution()
    x = s.trailingZeroes(4)
    print(x)
    x = s.trailingZeroes(6)
    print(x)
    x = s.trailingZeroes(21)
    print(x)
    x = s.trailingZeroes(26)
    print(x)
    x = s.trailingZeroes(180854)
    print(x)
    x = s.trailingZeroes(1808548)
    print(x)
    x = s.trailingZeroes(18085483)
    print(x)
    x = s.trailingZeroes(1808548329)
    print(x)

if __name__ == '__main__':
    test()
