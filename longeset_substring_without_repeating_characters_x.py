#!/usr/bin/env python

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        res = 0
        cur = 0
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                cur += 1
            else:
                print(i - d[c])
                print(cur + 1)
                cur = min(i - d[c], cur + 1)
                # cur = i - d[c]
            d[c] = i
            res = max(res, cur)
        return res



def test():
    s = Solution()
    a = s.lengthOfLongestSubstring('abcabcbb')
    print(a)
    a = s.lengthOfLongestSubstring('bbb')
    print(a)
    a = s.lengthOfLongestSubstring('aacbcdefxx')
    print(a)
    assert s.lengthOfLongestSubstring('aacbcdefxx') == 2
    assert s.lengthOfLongestSubstring('abba') == 2


test()
