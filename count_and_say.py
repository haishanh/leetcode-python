#!/usr/bin/env python

class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)
        prev = s[0]
        i = 1
        count = 1
        new_s = ''
        if len(s) == 1:
            return '1' + s[0]
        while i < len(s):
            curr = s[i]
            if prev == curr:
                count += 1
            else:
                new_s += str(count) + prev
                count = 1
            if i == len(s) - 1:
                new_s += str(count) + curr
            prev = curr
            i += 1
        return new_s

def test():
    s = Solution()
    # print(s.countAndSay(5))
    print(s.countAndSay(20))
    print('=' * 20)
    assert '1' == s.countAndSay(1)
    assert '11' == s.countAndSay(2)
    assert '21' == s.countAndSay(3)
    assert '111221' == s.countAndSay(5)
    print('Test passed!')


if __name__ == '__main__':
    test()
