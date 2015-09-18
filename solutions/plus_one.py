#!/usr/bin/env python

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        def carry(n):
            n[-1] = 0
            i = -2
            length = len(n)
            while -i <= length:
                if n[i] == 9:
                    n[i] = 0
                    i -= 1 # decrease i
                else:
                    n[i] += 1
                    return n
            n.insert(0, 1)
            return n
        return carry(digits)

def test():
    s = Solution()
    assert [1] == s.plusOne([0])
    assert [1, 0] == s.plusOne([9])
    assert [1, 0, 0] == s.plusOne([9, 9])
    assert [9, 9] == s.plusOne([9, 8])
    assert [1, 0, 0, 0] == s.plusOne([9, 9, 9])
    print('Test passed!')


if __name__ == '__main__':
    test()
