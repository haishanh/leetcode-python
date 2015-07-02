#!/usr/bin/env python

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if s == '':
            return 0
        x = s.split(' ')[::-1]
        for i in x:
            if i != '':
                return len(i)
        return 0


class Solution2:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        s = s.strip()
        if s == '':
            return 0
        return len(s.split(' ')[-1])


def test():
    s = Solution()
    assert 2 == s.lengthOfLastWord('b   ab')
    assert 1 == s.lengthOfLastWord('b   a    ')
    assert 3 == s.lengthOfLastWord('   day')
    s = Solution2()
    assert 2 == s.lengthOfLastWord('b   ab')
    assert 1 == s.lengthOfLastWord('b   a    ')
    assert 3 == s.lengthOfLastWord('   day')
    print('Test passed!')


if __name__ == '__main__':
    test()
