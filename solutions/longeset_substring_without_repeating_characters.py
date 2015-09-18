#!/usr/bin/env python

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        d = {}
        sub_str = []
        max_len = 0
        for i, c in enumerate(s):
            if c not in sub_str:
                sub_str.append(c)
            else:
                sub_str = list(s[d[c]+1:i])
                sub_str.append(c)
            d[c] = i
            max_len = max(max_len, len(sub_str))
        return max_len



def test():
    s = Solution()
    a = s.lengthOfLongestSubstring('abcabcbb')
    assert(a == 3)
    print(a)
    a = s.lengthOfLongestSubstring('bbb')
    assert(a == 1)
    print(a)
    a = s.lengthOfLongestSubstring('aacbcdefxx')
    assert(a == 6)
    print(a)
    a = s.lengthOfLongestSubstring('abba')
    assert(a == 2)
    print(a)


test()
